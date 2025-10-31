from django.db import models
from django.contrib.auth.models import User # Importe o modelo de usuário

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.titulo