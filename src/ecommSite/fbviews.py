from pyrebase import pyrebase 
from django.shortcuts import render
# from .views import views




fbconfig = {
    'apiKey': "AIzaSyCG9CEMR4ClQpP_X2dDkm9zOf9f2s6Q_Mk",
    'authDomain': "artini-22c83.firebaseapp.com",
    'databaseURL': "https://artini-22c83.firebaseio.com",
    'projectId': "artini-22c83",
    'storageBucket': "artini-22c83.appspot.com",
    'messagingSenderId': "850015264518",
    'appId': "1:850015264518:web:a0992497b42dec2f320887",
    'measurementId': "G-XE11DK6PDX"
}

firebase = pyrebase.initialize_app(fbconfig)
auth = firebase.auth()


def singIn(request):

    return render(request, "login.html")

def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
        # html = """

        # """
    except:
        message = "invalid cerediantials"
        return render(request,"auth/login.html",{"msg":message})
    print(user)
    return render(request, "welcome.html",{"e":email})

def register(request):
    return render(request,  "auth/register.html")

def newUser(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")

    auth.create_user_with_email_and_password(email, passw)

    return render(request, "welcome.html",{"e":email})
