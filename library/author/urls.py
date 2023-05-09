from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('author_list/', views.AuthorListView.as_view(), name='author_list'),
    path('create_author/', views.create_author, name='create_author'),
    path('delete_author/<int:author_id>/', views.delete_author, name='delete_author'),
]
