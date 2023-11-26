from django.contrib import admin

from blog.models import Articulo, Category

# Register your models here.

admin.site.register(Articulo)
admin.site.register(Category)
