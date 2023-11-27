from typing import Any
from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.db.models import Q

from blog.models import Articulo, Category


# Create your views here.


def home_page(request):
    articulos = Articulo.objects.filter(
        pub_date__lte=timezone.now()
    )
    categories = Category.objects.all()
    featured = Articulo.objects.filter(featured=True).filter(
        pub_date__lte=timezone.now()
    )[:3]
    
    context = {
        'articulos': articulos,
        'categories': categories,
        'featured': featured

    }

    return render(request, 'blog/home_page.html', context=context)


class ArticleDetailView(generic.DetailView):
    model = Articulo
    queryset = Articulo.objects.filter(
        pub_date__lte=timezone.now()
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class AboutMeView(generic.TemplateView):
    template_name = 'blog/about_me.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

