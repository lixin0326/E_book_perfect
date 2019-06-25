from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from account.context_processors import shop_count
from apps.comments.models import Book2
from apps.car.models import ShopCar


@csrf_exempt
def add(request):
    if request.is_ajax():
        if request.user.is_authenticated():
            try:
                book_id = request.POST.get('book_id')
                book_number = request.POST.get('number')
                uid = request.user.userprofile.uid
                cars = ShopCar.objects.filter(user_id=uid, book=book_id, status=1)
                if cars:
                    car = cars.first()
                    car.book_number = F('book_number') + book_number
                    # car.number += number
                    car.save(update_fields=['book_number'])
                    # ShopCar.objects.select_for_update 高并发
                else:
                    car = ShopCar(user_id=uid, book=book_id, book_number=book_number)
                    car.save()
                data = shop_count(request)
                data['status'] = 200
                data['msg'] = 'success'
                return JsonResponse(data=data)
            except Exception as e:
                return JsonResponse(data={'status': 404, 'msg': 'error'})
        else:
            # 表示没有登录
            return JsonResponse(data={'status': 401,
                                      'msg': 'error',
                                      'url': '/account/login/'})
    else:
        # 表示不是ajax请求
        return HttpResponse('不是ajax请求!')


@csrf_exempt
def delete(request):
    try:
        car_id = request.GET.get('car_id')
        car = ShopCar.objects.get(bc_id=car_id, status=1)
        car.status = -1
        car.save(update_fields=['status'])
        return redirect('http://127.0.0.1:8688/car/list_result/')
    except:
        return HttpResponse("移除商品失败!")


@login_required
def list_result(request):
    cars = ShopCar.objects.filter(user_id=request.user.userprofile.uid, status=1)
    car_info_list = [(car.book, car.book_number, car.bc_id) for car in cars]
    books = []
    for (book, book_number, bc_id) in car_info_list:
        book = Book2.objects.filter(book_id=book).first()
        book_dict = dict(
            book=book,
            bc_id=bc_id,
            book_number=book_number,
            book_name=book.book_name,
            image_url=book.image_url,
            price=book.price,
            author=book.author,
        )
        books.append(book_dict)
    return render(request, 'car_book.html', {'books': books})


@login_required
def update_num(request):
    pass
