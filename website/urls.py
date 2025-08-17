from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('especialidades/', views.especialidades, name='especialidades'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
]