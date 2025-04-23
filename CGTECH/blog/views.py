from django.shortcuts import render
from .models import Postagem
# Create your views here.

def listar_postagens(request):
    postagens = Postagem.objets.all()
    return render(request, 'blog/listar_postagens.html', {'postagens':postagens})