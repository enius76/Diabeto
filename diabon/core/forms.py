from django import forms


class GlycForm(ModelForm):
    class Meta:
    	model = Glyc
    	fields = ['value', 'note']

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
