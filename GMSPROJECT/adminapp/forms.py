from django import forms
from .models import User, Grievance, About, Contact, Usage, Notification
class AddUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
        exclude={"aid"}
class PostGreForm(forms.ModelForm):
    class Meta:
        model=Grievance
        fields ="__all__"
        exclude = {"user", "aid", "area", "name", "phno", "viewflag", "solvedflag", "postdt", "viewdt", "solvedt", "solvedby"}

class AboutForm(forms.ModelForm):
    class Meta:
        model=About
        fields="__all__"
        exclude = {"sid"}
        labels={"about": "ENTER ABOUT CONTENT"}

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"
        exclude={"sid"}
        labels={"about": "ENTER CONTACT CONTENT"}

class UsageForm(forms.ModelForm):
    class Meta:
        model=Usage
        fields="__all__"
        exclude = {"sid"}
        labels={"about": "HOW TO USE WEBSITE"}

class NotifyForm(forms.ModelForm):
    class Meta:
        model=Notification
        fields="__all__"
        exclude={"touser", "status", "senddt", "sendby"}
        labels={"notify":"NOTIFICATION TO BE SEND"}