from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    imagem = models.CharField(max_length=255, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome