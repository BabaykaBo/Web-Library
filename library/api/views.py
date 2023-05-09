from django.http import Http404
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from authentication.models import CustomUser
from author.models import Author
from book.models import Book, AuthorBook
from order.models import Order

from .serializers import UserSerializer, OrderSerializer, BookSerializer, AuthorSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class UserOrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Order.objects.filter(user=user_id)

    def get_object(self):
        user_id = self.kwargs['user_id']
        order_id = self.kwargs['pk']
        try:
            order = Order.objects.get(user=user_id, id=order_id)
        except Order.DoesNotExist:
            raise Http404('Order does not exist')

        return order
