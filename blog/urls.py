from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('',views.home_page),
    path('article/<slug:slug>', views.ArticleDetailView.as_view(), name="article"),
    path('about/', views.AboutMeView.as_view(), name='about_me'),
]
