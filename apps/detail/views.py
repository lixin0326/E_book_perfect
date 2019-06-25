from django.shortcuts import render
from apps.comments.models import Book2, Book_Chapter


def detail(request):
    book_id = request.GET.get('book_id')
    if book_id:
        books = Book2.objects.get(book_id=book_id)
        chapter = Book_Chapter.objects.filter(book_id=book_id)
        return render(request, 'detail.html', {'books': books,
                                               'chapter': chapter})
