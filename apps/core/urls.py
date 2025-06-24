from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_botanical, name='create_botanical'),
]
