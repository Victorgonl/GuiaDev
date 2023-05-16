from django import forms

class FormTutorial(forms.Form):
  id = forms.CharField(max_length=20, required=False)
  like = forms.CharField(required=False)
  copy = forms.CharField(required=False)
  pesquisa = forms.CharField(max_length=500, required=False)
  