from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm, LoginForm






# fbconfig = {
#     'apiKey': "AIzaSyCG9CEMR4ClQpP_X2dDkm9zOf9f2s6Q_Mk",
#     'authDomain': "artini-22c83.firebaseapp.com",
#     'databaseURL': "https://artini-22c83.firebaseio.com",
#     'projectId': "artini-22c83",
#     'storageBucket': "artini-22c83.appspot.com",
#     'messagingSenderId': "850015264518",
#     'appId': "1:850015264518:web:a0992497b42dec2f320887",
#     'measurementId': "G-XE11DK6PDX"
# }

# firebase = pyrebase.initialize_app(fbconfig)
# auth = firebase.auth()

# def singIn(request):
#     return render(request, "signIn.html")

# def postsign(request):
#     email=request.POST.get('email')
#     passw = request.POST.get("pass")
#     try:
#         user = auth.sign_in_with_email_and_password(email,passw)
#     except:
#         message = "invalid cerediantials"
#         return render(request,"signIn.html",{"msg":message})
#     print(user)
#     return render(request, "welcome.html",{"e":email})

def home_page(request):
    context = {
        "title":"Homepage"
    }
    return render(request, "home_page.html", context )

def about_page(request):
    context = {
        "title":"About"
    }
    return render(request, "about_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('fullName'))
    return render(request, "contact/view.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    context = {
        "form":form
    }
    return render(request, "auth/login.html", context)

def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", {})

def welcome_page(request):
    form = LoginForm(request.POST or None)
    
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "welcome.html", {})

def home_page_old(request):
    html_ = """
    <!doctype html>
    <html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

        <title>Hello, world!</title>
    </head>
    <body>
        <div class='text-center'>
        <h1>Hello, world!</h1>
        </div>
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </body>
    </html>
    """
    return HttpResponse(html_)