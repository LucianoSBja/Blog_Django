from django.urls import path
from django.views.generic import TemplateView

from perfiles import views 

app_name = 'perfiles'

urlpatterns = [
    path('registration/', views.PerfilRegistration.as_view(), name='registration' ),
    path('success/', TemplateView.as_view(template_name='perfiles/success_registration.html'), name='success')
]
