from django import forms

from author.models import Author
from book.models import Book


class AuthorForm(forms.ModelForm):
    books = forms.ModelMultipleChoiceField(queryset=Book.objects.all(), required=False)

    class Meta:
        model = Author
        fields = ('name', 'surname', 'patronymic')

