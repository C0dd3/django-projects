from django.db import models

# Create your models here.
class Produto(models.Model): # Adicionando uma classe para models.
    nome = models.CharField(max_length=200) # Define o número max de caracteres.
    preco = models.DecimalField(max_digits=5, decimal_places=2) # Denfine as casa e número de digitos.
    descricao = models.TextField() # Valor infinitos de caracteres.

    def __str__(self): # Função de verificar valor dentro da app.
        return self.nome