from datetime import datetime

from django.shortcuts import render, redirect

from books.models import Book


def books_view_index(request):
    return redirect('books')
def books_view(request):
    template = 'catalog.html'
    book = Book.objects.all()
    context = {'books': book}
    return render(request, template, context)



def book_view_detail(request, pub_date: datetime):
    template = 'product.html'

    book = Book.objects.filter(pub_date=pub_date)

    try:
        next_page = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    except:
        next_page = ''
    try:
        previous_page = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    except:
        previous_page = ''

    context = {'book': book, 'previous_page': previous_page, 'next_page': next_page}
    return render(request, template, context)