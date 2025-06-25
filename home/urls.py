from django.urls import path
from . import views

urlpatterns = [
    path('credits', views.credits, name='credits'),
    path('about', views.about, name='about'),
    path('version', views.version, name='version'),
]
