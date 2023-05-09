from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, AuthorViewSet, BookViewSet, OrderViewSet, UserOrderViewSet

router = DefaultRouter()
router.register('user', UserViewSet)
router.register('order', OrderViewSet)
router.register('book', BookViewSet)
router.register('author', AuthorViewSet)
# urlpatterns = [
#     path('user/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
#     path('user/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='user-detail'),
#
    # path('user/<int:user_id>/order/', UserOrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-order-list'),
    # path('user/<int:user_id>/order/<int:pk>/', UserOrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='user-order-detail'),
#
#     path('order/', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='order-list'),
#     path('order/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='order-detail'),
#
#     path('book/', BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='book-list'),
#     path('book/<int:pk>/', BookViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='book-detail'),
#
#     path('author/', AuthorViewSet.as_view({'get': 'list', 'post': 'create'}), name='author-list'),
#     path('author/<int:pk>/', AuthorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='author-detail'),
# ]

urlpatterns = [
    path('user/<int:user_id>/order/', UserOrderViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='user-order-list'),

    path('user/<int:user_id>/order/<int:pk>/',
         UserOrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='user-order-detail'),

    path('', include(router.urls))
]
