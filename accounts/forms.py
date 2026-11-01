
from django import forms
from django.contrib.auth.models import User
import re

class SignupForm(forms.ModelForm):
    phone=forms.CharField(max_length=15)
    password=forms.CharField(widget=forms.PasswordInput,min_length=8)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username","email","password"]

    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get("password")
        confirm_password=cleaned_data.get("confirm_password")

        if password:
            if len(password)<8:
                self.add_error("password","Password must contain at least 8 characters")
            if not re.search(r'[A-Z]',password):
                self.add_error("password","Include at least one uppercase letter")
            if not re.search(r'[a-z]',password):
                self.add_error("password","Include at least one lowercase letter")
            if not re.search(r'[0-9]',password):
                self.add_error("password","Include at least one number")
            if not re.search(r'[^A-Za-z0-9]',password):
                self.add_error("password","Include at least one special character")

        if password and confirm_password:
            if password!=confirm_password:
                self.add_error("confirm_password","Passwords do not match")

        return cleaned_data
