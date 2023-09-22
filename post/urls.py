from django.urls import path
from .views import create_post, edit_post, delete_post

urlpatterns = [
    path('add/', create_post, name='add_post'),
    path('edit/<int:id>', edit_post, name='edit_post'),
    path('delete/<int:id>', delete_post, name='delete_post')
]