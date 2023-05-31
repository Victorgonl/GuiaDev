from django import forms

class FormTutorial(forms.Form):
  id = forms.CharField(max_length=20, required=False)
  like = forms.CharField(required=False)
  copy = forms.CharField(required=False)
  pesquisa = forms.CharField(max_length=500, required=False)
  nome_autor = forms.CharField(max_length=50, required=False)
  comentario = forms.CharField(max_length=500, required=False)
  sair = forms.CharField(max_length=20, required=False)

class FormLogin(forms.Form):
  login = forms.CharField(max_length=50, required=False)
  senha = forms.CharField(max_length=50, required=False)