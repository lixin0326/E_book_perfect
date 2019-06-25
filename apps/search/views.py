from django.shortcuts import render, HttpResponse

from apps.comments.models import Book2


def search(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        books = Book2.objects.filter(book_name__icontains=keyword).values('book_id', 'book_name', 'author', 'price',
                                                                          'image_url', 'info').order_by('book_id')
        # for book in books:
        #     img = Book2.objects.filter(book_id=book.get('book_id')).first()
        #     book.update(image_url=img)

        return render(request, 'search_result.html', {'books': books})
    else:
        return HttpResponse("没有搜索到相关书籍!")
