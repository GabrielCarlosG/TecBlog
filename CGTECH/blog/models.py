from django.db import models

# Create your models here.
class Postagem(models.Model):
    titulo = models.charfild(max_length=255)
    data_postagem = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to='imagens/')
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo