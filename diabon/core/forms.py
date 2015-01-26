from django import forms


class GlycForm(ModelForm):
    class Meta:
    	model = Glyc
    	fields = ['value', 'note']