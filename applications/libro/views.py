from django.shortcuts import render
from django.views.generic import ListView
from .models import Libro
# Create your views here.

class ListLibros(ListView):
    template_name='libro/lista.html'
    context_object_name='libros'

    def get_queryset(self):
        keyword=self.request.GET.get('keyword', '')

        #Fecha de inicio
        startDate=self.request.GET.get('startDate','')
        #Fecha de finalización
        finishDate=self.request.GET.get('finishDate','')
        
        if not startDate and  not finishDate:        
            return Libro.objects.filterByDate(keyword)
        else:
            return Libro.objects.filterByDate1(keyword, startDate, finishDate)