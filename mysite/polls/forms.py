from django import forms
from polls.models import Portfolio
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class PasswordChangedForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'size': '40','padding': '10px 15px','border-radius': '4px','height':'50px'}),label="Old Password")
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'size': '40'}),label="New Password")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'size': '40','color':'red'}),label="Confirm New Password")

    
class UserChangedForm(UserChangeForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['id','portfolio','description','url']