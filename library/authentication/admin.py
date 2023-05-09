from django.contrib import admin

from authentication.models import CustomUser
from author.models import Author
from book.models import Book, AuthorBook
from order.models import Order


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'id', 'first_name', 'middle_name', 'last_name', 'created_at', 'is_active', 'role']
    ordering = ('id', 'email', 'first_name')


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book', 'created_at', 'plated_end_at', 'end_at']
    ordering = ('id', 'user')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'surname', 'patronymic']
    ordering = ('id', 'name')
    fields = [('name', 'patronymic'), 'surname']


class ABAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'author']
    ordering = ('id', 'book')


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'count', 'author_list']
    ordering = ('id', 'name')
    list_filter = ('id', 'name', 'authors__name')
    readonly_fields = ('author_list',)

    def author_list(self, obj):
        return ", ".join([author.name + " " + author.surname for author in obj.authors.all()])

    def get_readonly_fields(self, request, obj=None):
        # Make the name and authors fields read-only in the detail view
        if obj:
            return ['name', 'author_list'] + list(self.readonly_fields)
        return self.readonly_fields

    fieldsets = (
        (None, {'fields': ('name', 'author_list')}),
        ('Available', {'fields': ('description', 'count')})
    )

    author_list.short_description = 'Authors'


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(AuthorBook, ABAdmin)
admin.site.register(Order, OrderAdmin)
