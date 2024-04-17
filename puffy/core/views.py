from django.shortcuts import render

from item.models import Categoria, Item

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categorias = Categoria.objects.all()

    return render (request, 'core/index.html', {
        'categorias': categorias,
        'items': items,
    })

def contato(request):
    return render (request, 'core/contato.html')