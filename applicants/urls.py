from django.urls import path

from . import views

app_name = "applicants"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("sign-in", views.SignIn.as_view(), name="sign_in"),
    path("sign-out", views.SignOut.as_view(), name="sign_out"),
    path("sign-up", views.SignUp.as_view(), name="sign_up"),
    path("reset", views.ResetPassword.as_view(), name="reset_password"),
    path("submit", views.SubmitApplication.as_view(), name="submit_application"),
    path("get-application", views.GetApplication.as_view(), name="get_application"),

]