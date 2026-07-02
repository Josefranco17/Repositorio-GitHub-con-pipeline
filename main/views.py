from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookForm
from .models import Book


def _get_cart(request):
    return request.session.get('cart', {})


def _save_cart(request, cart):
    request.session['cart'] = cart
    request.session.modified = True


def book_list(request):
    books = Book.objects.order_by('-published_date', 'title')
    return render(request, 'main/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'main/book_detail.html', {'book': book})


def book_create(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        book = form.save()
        return redirect('book_detail', pk=book.pk)
    return render(request, 'main/book_form.html', {'form': form, 'create': True})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)
    if request.method == 'POST' and form.is_valid():
        book = form.save()
        return redirect('book_detail', pk=book.pk)
    return render(request, 'main/book_form.html', {'form': form, 'create': False, 'book': book})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'main/book_confirm_delete.html', {'book': book})


def cart_add(request, pk):
    book = get_object_or_404(Book, pk=pk)
    cart = _get_cart(request)
    cart[str(book.pk)] = cart.get(str(book.pk), 0) + 1
    _save_cart(request, cart)
    return redirect('cart_detail')


def cart_remove(request, pk):
    cart = _get_cart(request)
    cart.pop(str(pk), None)
    _save_cart(request, cart)
    return redirect('cart_detail')


def cart_clear(request):
    _save_cart(request, {})
    return redirect('cart_detail')


def cart_detail(request):
    cart = _get_cart(request)
    book_ids = [int(pk) for pk in cart.keys()]
    books = Book.objects.filter(pk__in=book_ids)
    items = []
    for book in books:
        quantity = cart.get(str(book.pk), 0)
        items.append({'book': book, 'quantity': quantity})
    total_items = sum(item['quantity'] for item in items)
    return render(request, 'main/cart.html', {
        'items': items,
        'total_items': total_items,
    })
