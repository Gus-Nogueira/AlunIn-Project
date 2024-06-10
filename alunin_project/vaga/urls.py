from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:vaga_id>/', views.detail, name='detalhes'),
    path('<int:vaga_id>/apply/', views.apply, name='aplicar'),
]
