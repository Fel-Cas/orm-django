from django.shortcuts import render
#modelo local
from .models import Autor
#lista generica
from django.views.generic import ListView

# Create your views here.

class ListAutores(ListView):
    template_name = 'autor/lista.html'
    context_object_name='autores'

    def get_queryset(self):
        keyword=self.request.GET.get('keyword', '')
        author=Autor.objects.filterByAge()
        return author