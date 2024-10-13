from django import forms
from .models import Cliente  # Certifique-se de que o modelo Cliente está definido

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'numero_identificacao_fiscal', 'morada', 'codigo_postal', 'localidade', 'telefone', 'email', 'website']
