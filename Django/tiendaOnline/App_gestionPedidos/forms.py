from django import forms

class Formulario_Contacto(forms.Form):

    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()
    