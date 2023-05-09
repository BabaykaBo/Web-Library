from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from .forms import AuthorForm
from .models import Author


@method_decorator(user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('403')), name='dispatch')
class AuthorListView(ListView):
    model = Author
    context_object_name = "author_list"
    template_name = 'author/author_list.html'
    ordering = ['name']


@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('403'))
def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()

            for book in form.cleaned_data['books']:
                book.authors.add(author)

            return redirect('authors:author_list')

        else:
            error_message = "Invalid author creation"
            context = {'form': form, 'error_message': error_message}
            return render(request, 'author/create_author.html', context)

    else:
        form = AuthorForm()

    context = {'form': form}
    return render(request, 'author/create_author.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('403'))
def delete_author(request, author_id):
    author = Author.objects.get(id=author_id)
    author.delete()
    return redirect('authors:author_list')
