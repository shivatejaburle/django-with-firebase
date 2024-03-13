from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
import pyrebase
from django.contrib import auth
from applicants.forms import SignInForm, SignUpForm, ResetPasswordForm, ApplicationForm
from django.contrib import messages

import time
from datetime import datetime, timezone
import pytz
from django.core.files.storage import default_storage

# Firebase
firebase = pyrebase.initialize_app(settings.CONFIG)
authentication = firebase.auth()
database = firebase.database()
storage = firebase.storage()

class IndexView(View):
    template_name = 'applicants/index.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
class SignIn(View):
    template_name = 'applicants/sign_in.html'
    success_url = 'applicants:index'

    def get(self, request):
        form = SignInForm()
        context = {'form':form}
        return render(request, self.template_name, context)
    
    def post(self, request):
        get_email = request.POST['email']
        get_password = request.POST['password']
        
        try:
            user = authentication.sign_in_with_email_and_password(get_email, get_password)
        except:
            form = SignInForm(request.POST)
            context = {'form':form}
            messages.error(request, "Invalid Credentials !")     
            return render(request, self.template_name, context)
        
        session_id = user['idToken']
        request.session['uid'] = str(session_id)

        if not 'uid' in request.session:
            return redirect('applications:sign_in')
        else:
            user_data = database.child("users").child(user['localId']).child('details').child('name').get()
            request.session['displayName'] = user_data.val()
            
            count_submissions = 0
            try:
                user_submissions = database.child("users").child(user['localId']).child('submission').get()
                for item in user_submissions:
                    count_submissions += 1
                request.session['total_submissions'] = count_submissions
            except:
                request.session['total_submissions'] = count_submissions
            
            messages.success(request, "Login Success !")
            return redirect(self.success_url)

class SignOut(View):
    success_url = "applicants:sign_in"

    def get(self, request):
        auth.logout(request)
        request.session.clear()
        request.session.flush()
        messages.info(request, "Logout Success !")
        return redirect(self.success_url)

class SignUp(View):
    template_name = 'applicants/sign_up.html'
    success_url = 'applicants:sign_in'

    def get(self, request):
        form = SignUpForm()
        context = {'form':form}
        return render(request, self.template_name, context)
    
    def post(self, request):
        get_name = request.POST['name']
        get_email = request.POST['email']
        get_password = request.POST['password']

        form = SignUpForm(request.POST)
        context = {
                'form':form,
        }
        
        try:
            user = authentication.create_user_with_email_and_password(get_email, get_password)
        except:
            messages.error(request, "Unable to create account. Try again after sometime !")
            return render(request, self.template_name, context)
        
        uid = user['localId']
        data = {
            'name':get_name,
            'status': '1'
        }
        database.child('users').child(uid).child('details').set(data)

        return redirect(self.success_url)

class ResetPassword(View):
    template_name = 'applicants/reset_password.html'

    def get(self, request):
        form = ResetPasswordForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        get_email = request.POST['email']
        form = ResetPasswordForm()
        context = {
            'form': form
        }

        try:
            authentication.send_password_reset_email(get_email)
            messages.success(request, f"Reset password link sent to {get_email}, please check your mailbox !")
            return render(request, self.template_name, context)
        except:
            messages.error(request, f"Something went wrong, Please check the email you provided is registered or not !")
            return render(request, self.template_name, context)

class SubmitApplication(View):
    template_name = 'applicants/application_form.html'
    success_url = 'applicants:index'
    fail_url = 'applicants:sign_in'

    def get(self, request):
        if not 'uid' in request.session:
            return redirect(self.fail_url)
        else:
            form = ApplicationForm()
            context = {'form':form}
            return render(request, self.template_name, context)
    
    def post(self, request):
        get_name = request.POST['name']
        get_email = request.POST['email']
        get_phone = request.POST['phone']
        file = request.FILES['file']
        
        # Save file to local Storage
        file_save = default_storage.save(file.name, file)

        # Get the extension of the uploaded file
        fileType = (file.name).split(".")[-1]
        
        # Upload Image
        storage.child(file_save).put(file_save)

        # Download Image
        import os
        storage.child(file_save).download(filename=file.name, path=os.path.basename(file_save))
        
        # Get url of image
        fileUrl = storage.child(file_save).get_url(request.session['uid'])

        # Delete local file
        default_storage.delete(file.name)
        
        tz= pytz.timezone('Asia/Kolkata')
        time_now= datetime.now(timezone.utc).astimezone(tz)
        ms = int(time.mktime(time_now.timetuple()))
        print("MILLISECONDS: "+str(ms))

        idToken= request.session['uid']
        a = authentication.get_account_info(idToken)
        a = a['users']
        a = a[0]
        a = a['localId']
        print("INFO: "+str(a))
        data = {
            "name":get_name,
            'email':get_email,
            'phone':get_phone,
            'fileType': fileType,
            'fileUrl' : fileUrl
        }
        database.child('users').child(a).child('submission').child(ms).set(data)

        user_submissions = database.child("users").child(a).child('submission').get()
        count_submissions = 0
        for item in user_submissions:
            count_submissions += 1
        request.session['total_submissions'] = count_submissions

        messages.success(request, "Application Submitted Successfully !")
        return redirect(self.success_url)
        
class GetApplication(View):
    template_name = "applicants/get_application_details.html"

    def get(self, request):

        idToken = request.session['uid']
        a = authentication.get_account_info(idToken)
        a = a['users']
        a = a[0]
        a = a['localId']
        application_data = database.child("users").child(a).child('submission').get()
        
        for i in application_data:
            name = database.child("users").child(a).child('submission').child(i.key()).child('name').get().val()
            email = database.child("users").child(a).child('submission').child(i.key()).child('email').get().val()
            phone = database.child("users").child(a).child('submission').child(i.key()).child('phone').get().val()
            fileType = database.child("users").child(a).child('submission').child(i.key()).child('fileType').get().val()
            fileUrl = database.child("users").child(a).child('submission').child(i.key()).child('fileUrl').get().val()

        context = {
            'name' : name,
            'email' : email,
            'phone' : phone,
            'fileType': fileType,
            'fileUrl' : fileUrl
        }
        return render(request, self.template_name, context)