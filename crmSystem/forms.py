from allauth.account.forms import LoginForm, ChangePasswordForm, ResetPasswordForm, ResetPasswordKeyForm, \
    SetPasswordForm
from crispy_forms.helper import FormHelper
from django import forms


class UserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields['login'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Introdu numele de utilizator', 'id': 'username'})
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2 position-relative', 'placeholder': 'Introdu parola', 'id': 'password'})
        self.fields['remember'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})

        self.fields['login'].label = 'Nume utilizator'
        self.fields['password'].label = 'Parolă'


class PasswordChangeForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields['oldpassword'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Introdu parola veche', 'id': 'password2'})
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Introdu parola nouă', 'id': 'password3'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Confirmă parola nouă', 'id': 'password4'})

        self.fields['oldpassword'].label = 'Parolă veche'
        self.fields['password1'].label = 'Parolă nouă'
        self.fields['password2'].label = 'Confirmă parola nouă'


class PasswordResetForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Introdu adresa de e-mail', 'id': 'email'})

        self.fields['email'].label = 'E-mail'


class PasswordResetKeyForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetKeyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Introdu parola nouă', 'id': 'password5'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Confirmă parola nouă', 'id': 'password6'})

        self.fields['password1'].label = 'Parolă nouă'
        self.fields['password2'].label = 'Confirmă parola nouă'


class PasswordSetForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(PasswordSetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Introdu parola nouă', 'id': 'password7'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Confirmă parola nouă', 'id': 'password8'})

        self.fields['password1'].label = 'Parolă nouă'
        self.fields['password2'].label = 'Confirmă parola nouă'
