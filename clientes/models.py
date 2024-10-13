from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    numero_identificacao_fiscal = models.CharField(max_length=50)
    morada = models.CharField(max_length=255)
    codigo_postal = models.CharField(max_length=20)
    localidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True)

    def __str__(self):
        return self.nome
