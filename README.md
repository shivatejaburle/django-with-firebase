# Django with Firebase

Building a Seamless Django Application Integrated with Firebase: Empowering Users to Create Accounts, Log In with Username and Password, Log Out, Reset Passwords, and Effortlessly Store and Retrieve Data and Media Files (.jpg, .png, .pdf, .docx).

## Functionality

- Create an account
- Log in via username & password
- Log out
- Reset password
- Store and retrieve data from Firebase
- Store and retrieve media (.jpg, .png, .pdf, .docx) from Firebase

## Setup Firebase

### Create Project

| Click on Create Project | Enter Project Name | Enable Analytics |  Choose Analytics Location|
| -------------|-------------------|------------|------------|
|<img src="./screenshots/firebase/01-Firebase-console.jpg">| <img src="./screenshots/firebase/02-Create-project.jpg">  | <img src="./screenshots/firebase/03-Create-project.jpg">| <img src="./screenshots/firebase/04-Create-project-Firebase-console.jpg"> |

### Create Application

| Click on Continue | Add Application | Register App | Firebase SDK |
| -------------|-------------------|------------|------------|
| <img src="./screenshots/firebase/05-Create-project.jpg">  | <img src="./screenshots/firebase/06-applicant-registrations-Overview.jpg">| <img src="./screenshots/firebase/07-applicant-registrations-Add-app.jpg"> | <img src="./screenshots/firebase/08-applicant-registrations-Add-app.jpg"> |

### Create Realtime Database

| Build - Realtime Database | Create Database | Choose Database Location | Security Rules |
| -------------|-------------------|------------|------------|
| <img src="./screenshots/firebase/09-applicant-registrations-Overview.jpg">  | <img src="./screenshots/firebase/10-applicant-registrations-Realtime-Database.jpg">| <img src="./screenshots/firebase/11-applicant-registrations-Realtime-Database.jpg"> | <img src="./screenshots/firebase/12-applicant-registrations-Realtime-Database.jpg"> |

### Create Storage

| Build - Storage | Create Storage | Security Rules | Choose Location |
| -------------|-------------------|------------|------------|
| <img src="./screenshots/firebase/13-applicant-registrations-Overview.jpg">  | <img src="./screenshots/firebase/14-applicant-registrations-Storage.jpg">| <img src="./screenshots/firebase/15-applicant-registrations-Storage.jpg"> | <img src="./screenshots/firebase/16-applicant-registrations-Storage.jpg"> |

### Storage Rules and Authentication

| Storage Rules | Build - Authentication | Choose Sign Provider | Enable Sign-in  |
| -------------|-------------------|------------|------------|
| <img src="./screenshots/firebase/17-applicant-registrations-Storage-rules.jpg">  | <img src="./screenshots/firebase/18-applicant-registrations-Authentication.jpg">| <img src="./screenshots/firebase/19-applicant-registrations-Authentication-Sign-in-method.jpg"> | <img src="./screenshots/firebase/20-applicant-registrations-Authentication-Sign-in-method.jpg">


## Installing

### Clone the project

```bash
git clone https://github.com/shivatejaburle/django-with-firebase
cd django-with-firebase
```

### Setup your Virtual Environment
```bash
pip install virtualenv
virtualenv venv
# For Windows
venv\Scripts\activate   
# For Mac
source venv/bin/activate 
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Environment Settings

Create `django-with-firebase/.env` to store Firebase Configurations.

```bash
API_KEY = "Your-API-Key"
AUTH_DOMAIN = "AUTH_DOMAIN"
PROJECT_ID = "PROJECT_ID"
STORAGE_BUCKET = "STORAGE_BUCKET"
MESSAGING_SENDER_ID = "MESSAGING_SENDER_ID"
APP_ID = "APP_ID"
DATABASE_URL = "DATABASE_URL"
```

### Apply migrations

```bash
python manage.py migrate
```
### Collect static files (only on a production server)

```bash
python source/manage.py collectstatic
```

### Running a development server

Just run this command:

```bash
python manage.py runserver
```

## Screenshots

| Landing Page | Create an Account in Firebase | Login Page |
| -------------|-------------------|------------|
|<img src="./screenshots/app/A1-Landing-page.jpg">| <img src="./screenshots/app/A2-Create-Account.jpg">  | <img src="./screenshots/app/A3-Login.jpg">|

| Home Page | Submit Application (with Image) | Submission Success |
| -------------|-------------------|------------|
|<img src="./screenshots/app/A4-Home-Page.jpg">| <img src="./screenshots/app/A5-Submit-Application.jpg">  | <img src="./screenshots/app/A6-Submit-Success.jpg">|

| View Application (with Image) | Submit Application (with PDF) | View Application (with PDF) |
| -------------|-------------------|------------|
|<img src="./screenshots/app/A7-Get-Application-with-Image.jpg">| <img src="./screenshots/app/A8-Submit-Application.jpg">  | <img src="./screenshots/app/A9-Get-Application-with-pdf.jpg">|

| Submit Application (with DOCX) | View Application (with DOCX) | View DOCX |
| -------------|-------------------|------------|
|<img src="./screenshots/app/A10-Submit-Application-with-doc.jpg">| <img src="./screenshots/app/A11-A9-Get-Application-with-docx.jpg">  | <img src="./screenshots/app/A12-View-doc.jpg">|

| Data at Firebase Realtime Database | Media at Firebase Storage | Reset Password |
| -------------|-------------------|------------|
|<img src="./screenshots/app/A13-Firebase-Database.jpg">| <img src="./screenshots/app/A14-Firebase-Storage.jpg">  | <img src="./screenshots/app/A15-reeset-password.jpg">|