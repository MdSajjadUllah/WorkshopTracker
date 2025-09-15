from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['workshop_name', 'location', 'phone', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class SigninForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
