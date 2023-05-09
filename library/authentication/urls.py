from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from . import views

app_name = 'auth'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('log_in/', views.log_in, name='log_in'),
    path('log_out/', auth_views.LogoutView.as_view(next_page='auth:loggedout'), name='log_out'),
    path('loggedout/', TemplateView.as_view(template_name='registration/loggedout.html'), name='loggedout'),
]

