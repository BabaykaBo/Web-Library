from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from book.models import Book
from authentication.models import CustomUser


@method_decorator(login_required, name='dispatch')
class UserListView(ListView):
    model = CustomUser
    context_object_name = "user_list"
    template_name = 'user/user_list.html'
    ordering = ['email']


@method_decorator(login_required, name='dispatch')
class UserDetailView(DetailView):
    model = CustomUser
    context_object_name = "user"
    template_name = 'user/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        books = Book.objects.filter(order__user=user)
        context['books'] = books
        return context
