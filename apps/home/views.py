from django.shortcuts import render
from apps.comments.models import Book2, Book_classify2
from wh1804_bookstore.settings import sinlogger


def home(request):
    sinlogger.debug("IndexHandler:enter.")
    classify = Book_classify2.objects.all()
    book = Book2.objects.filter(classify_id=1)
    return render(request, 'index.html', {'book': book,
                                          'classify': classify})


# 这里是购书指南
def book_guide(request):
    return render(request, 'home/buy_book.html')


def cat_home(request):
    classify = Book_classify2.objects.all()
    cid = int(request.GET.get('cid', 0))
    if cid == 0:
        return home(request)
    book = Book2.objects.filter(classify_id=cid)

    return render(request, 'index.html', {'book': book,
                                          'classify': classify,
                                          })
