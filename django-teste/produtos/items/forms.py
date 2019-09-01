from django import forms
from .models import Produto

# Arquivo para adicionar um model para dentro de um formulário.

class ProdutoForm(forms.ModelForm):

    class Meta:

        model = Produto
        fields = ['nome', 'preco', 'descricao']