from django.urls import path

from .views import create_category

urlpatterns = [
    path('add/', create_category, name='add'),
]