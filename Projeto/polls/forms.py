from django import forms

class FormTutorial(forms.Form):
  id = forms.CharField(max_length=500)
  like = forms.CharField(required=False)
  copy = forms.CharField(required=False)
  