from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from blog.models import Articulo, Category
# Create your views here.


def home_page(request):
    articulos = Articulo.objects.all()
    categories = Category.objects.all()
    featured = Articulo.objects.filter(featured=True)[:3]
    
    context = {
        'articulos': articulos,
        'categories': categories,
        'featured': featured

    }

    return render(request, 'blog/home_page.html', context=context)


class ArticleDetailView(generic.DetailView):
    model = Articulo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context 