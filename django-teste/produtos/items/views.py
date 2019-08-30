from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto
# Create your views here.

# Define um resposta para cada uma dos setores definidos:.
def home(request):
    mensagem = "Mensagem da view"
    produtos = Produto.objects.all() # "Equivalente a: SELECT * FROM Produto"

    return render(request, "items/index.html", {"msg":mensagem, "produtos":produtos}) # Adicionando mensagem dentro do template criado.

def produtos(request):
    return HttpResponse('<h1>Área de Produtos</h1>')

def clientes(request):
    return HttpResponse('<h1>Área de Clientes</h1>')