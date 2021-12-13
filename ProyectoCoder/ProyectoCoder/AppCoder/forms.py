from django import forms

class JugadorFormulario(forms.Form):
    apellido = forms.CharField(required=True)
    numero = forms.IntegerField()
    esBueno = forms.BooleanField()

