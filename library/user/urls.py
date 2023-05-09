from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.UserListView.as_view(), name='user_list'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
]