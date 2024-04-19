from django.shortcuts import render, redirect
from item.models import Categoria, Item
from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categorias = Categoria.objects.all()

    return render (request, 'core/index.html', {
        'categorias': categorias,
        'items': items,
    })

def contato(request):
    return render (request, 'core/contato.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {
       'form':form
       })