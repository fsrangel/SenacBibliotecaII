from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano_publicacao', 'categoria']

class PreferenciasForm(forms.Form):
    cor_fundo = forms.CharField(max_length=7, label='Cor de Fundo', widget=forms.TextInput(attrs={'type': 'color'}))