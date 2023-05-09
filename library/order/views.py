from datetime import datetime, timedelta

from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test, login_required

from django.views.generic import ListView


from .models import Order
from book.models import Book

from .forms import OrderCreationForm


@method_decorator(user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('403')), name='dispatch')
class AllOrderListView(ListView):
    model = Order
    context_object_name = "all_orders"
    template_name = 'order/all_orders.html'
    ordering = ['id']


@method_decorator(login_required, name='dispatch')
class MyOrderListView(ListView):
    model = Order
    context_object_name = "my_orders"
    template_name = 'order/my_orders.html'
    ordering = ['id']

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


@login_required
def create_order(request):
    # books = Book.objects.all()
    #
    # if request.method == 'POST':
    #     book_id = request.POST.get('book_id')
    #     user_id = request.user.id
    #     plated_end_at = datetime.now() + timedelta(days=15)
    #
    #     existing_order = Order.objects.filter(book_id=book_id, user_id=user_id).first()
    #     if existing_order:
    #         error_message = f"You have already ordered '{existing_order.book.name}' book."
    #         return render(request, 'order/create_order.html', {'error_message': error_message, 'books': books})
    #
    #     order = Order(book_id=book_id, user_id=user_id, plated_end_at=plated_end_at)
    #     order.save()
    #
    #     return redirect('orders:order_my')
    #
    # return render(request, 'order/create_order.html', {'books': books})

    books = Book.objects.all()

    if request.method == 'POST':
        form = OrderCreationForm(request.POST, instance=Order(user=request.user))
        if form.is_valid():
            form.save(commit=False)
            book = form.cleaned_data.get('book')
            user = request.user
            if Order.objects.filter(book=book.id, user=user.id).exists():
                context = {'form': form, 'error': f"You have already ordered '{book.name}' book."}
                return render(request, 'order/create_order.html', context)
            else:
                form.save()
                return redirect('orders:order_my')
        else:
            context = {'form': form, 'error': 'Order error'}
            return render(request, 'order/create_order.html', context)
    else:
        form = OrderCreationForm(instance=Order(user=request.user))

    return render(request, 'order/create_order.html', {'form': form, 'books': books})


@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('403'))
def close_order(request, order_id):
    order = Order.objects.get(id=order_id)

    order.end_at = datetime.now()
    order.save()
    return redirect('orders:order_all')

