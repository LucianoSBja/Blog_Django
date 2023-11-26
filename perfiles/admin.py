from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from perfiles.models import Perfil

# Register your models here.

admin.site.register(Perfil, UserAdmin)