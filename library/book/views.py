from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from book.models import Book


@method_decorator(login_required, name='dispatch')
class BookListView(ListView):
    model = Book
    context_object_name = "all_books"
    template_name = 'book/book_list.html'
    ordering = ['name', '-count']


@method_decorator(login_required, name='dispatch')
class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = 'book/book_detail.html'
    login_url = "auth:log_in"


@method_decorator(login_required, name='dispatch')
class BookSearchView(ListView):
    model = Book
    template_name = 'book/book_search.html'
    context_object_name = "books"

    def get_queryset(self):
        query = self.request.GET.get("search")

        object_list = Book.objects.filter(
            Q(name__icontains=query)
            | Q(authors__name__icontains=query)
            | Q(authors__surname__icontains=query)
            | Q(name__iexact=query)
            | Q(authors__name__iexact=query)
            | Q(authors__surname__iexact=query)).order_by('name', '-count').distinct()

        return object_list



