from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    cuerpo = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    overview = models.TextField()
    categories = models.ManyToManyField("Category")
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("blog:article", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return self.titulo

class Category(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse("blog:category", kwargs={"slug": self.slug})

    def __str__(self):
        return self.titulo