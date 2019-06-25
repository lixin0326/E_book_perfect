import datetime
import random

from alipay import AliPay
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from account.context_processors import shop_count
from apps.car.models import Order, ShopCar
from apps.comments.models import Book2
from wh1804_bookstore import settings

"""
拿到所有被选中的购物车记录
1>第一个 选择地址
2>第二个 选择支付方式
3>第三个 配送方式

提交订单
1>生成订单号
2>更新商品的库存量
3>购物车表

涉及到多个表  多个表的查询 使用关联查询

事务(所有操作要么全部成功,要么全部失败) 

原子性:所有操作要么全部成功,要不全部失败(回滚)
一致性:保持数据的完整性
隔离性:可以多个用户同时操作(注意隔离级别)
持久性:所有操作一旦操作成功,不可撤回

"""


@csrf_exempt
def order(request):
    if request.is_ajax():
        try:
            car_id_list = request.POST.get('bc_id')
            car_ids = car_id_list.split(',')
            for i in range(len(car_ids)):
                car = ShopCar.objects.get(bc_id=car_ids[i], status=1)
                car.status = -1
                car.save(update_fields=['status'])

            request.session['car_ids'] = car_ids

            data = shop_count(request)
            data['status'] = 200
            data['msg'] = 'success'
            return JsonResponse(data=data)

        except Exception as e:
            # 表示添加订单失败
            return JsonResponse(data={'status': 404, 'msg': 'error'})
    else:
        return HttpResponse("不是ajax请求!")


@csrf_exempt
def test_order(request):
    try:
        car_ids = request.session['car_ids']
        cars = ShopCar.objects.filter(bc_id__in=car_ids)

        car_info_list = [(car.book, car.book_number) for car in cars]
        books = []
        sumprice = 0

        for (book_id, book_number) in car_info_list:
            book = Book2.objects.filter(book_id=book_id).first()
            car_number = book_number
            car_price = book.price
            # 　每一条数据的总价
            sum_book_price = car_number * car_price
            # 最后实付的总价
            sumprice += sum_book_price

            book_dict = dict(
                book_id=book_id,
                book_number=book_number,
                book_name=book.book_name,
                author=book.author,
                price=book.price,
                image_url=book.image_url,
                sum_book_price=sum_book_price
            )

            books.append(book_dict)

        # 订单号
        order_code = f'{datetime.datetime.strftime(datetime.datetime.now(),"%Y%m%d%H%M%S")}{random.randint(10,99)}'
        # 　对订单表操作--修改商品的库存量--修改购物车表
        # 第一步 生成订单号(支付平台需要,站内唯一) 格式年月日时分秒
        date = datetime.datetime.now()
        with transaction.atomic():
            try:
                # 第二步 往订单表增加记录
                order = Order(order_code=order_code,
                              address='河南省商城县',
                              mobile='18736262608',
                              receiver='小雪慧',
                              user_message='呀呀呀',
                              create_date=date,
                              user_id=1)
                order.save()
            except Exception as e:
                return HttpResponse('订单生成失败!')

            return render(request, 'order.html', {'books': books,
                                                  'order_code': order_code,
                                                  'sumprice': sumprice})

    except Exception as e:
        return HttpResponse("还没有购买商品哦!亲")
