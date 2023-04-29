from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.produtos, name='produtos'),
    path('atualiza/<int:id>', views.atualiza, name='atualiza'),
]
