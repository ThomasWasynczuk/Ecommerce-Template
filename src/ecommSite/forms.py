from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "id":"fullnameid", "placeholder":"Full Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "id":"emailid", "placeholder":"Email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "id":"contentid", "placeholder":"Contact us"}))


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "id":"username", "placeholder":"Username"}))
    password = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "id":"password", "placeholder":"Password"}))

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "id":"username", "placeholder":"Username"}))
    password = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "id":"password", "placeholder":"Password"}))