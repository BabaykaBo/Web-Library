from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('all_orders', views.AllOrderListView.as_view(), name='order_all'),
    path('my_orders', views.MyOrderListView.as_view(), name='order_my'),
    path('create_order/', views.create_order, name='create_order'),
    path('close_order/<int:order_id>/', views.close_order, name='close_order'),
]