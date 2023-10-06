from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('animal/', views.animal_list, name='animal_list'),
    path('colaborador/', views.colaborador_list, name='colaborador_list'),
    path('protectora/', views.protectora_list, name='protectora_list'),
]
