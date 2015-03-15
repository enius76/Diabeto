# coding: utf-8
import re
from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

 
class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Nom d'utilisateur"), error_messages={ 'invalid': _("Ne peut contenir que des caracteres alphanumeriques [a-z+0-9].") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Adresse email"), error_messages={ 'invalid': _("Veuillez rentrer une adresse email valide.")})
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Mot de passe"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Mot de passe (confirmation)"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("Ce pseudo existe deja. Merci d'en choisir un nouveau"))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("Les 2 mots de passes ne correspondent pas"))
        return self.cleaned_data
