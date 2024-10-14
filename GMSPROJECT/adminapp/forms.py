from django import forms
from .models import User
class AddUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
        exclude={"aid"}