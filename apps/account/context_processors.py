# 如何自定义全局的模板变量
# 在app下新建一个context_processors.py文件
# 在文件中创建一个函数,根据业务逻辑返回字典对象
# 在setting的template中注册
from django.db.models import Sum

from apps.car.models import ShopCar


def shop_count(request):
    count = 0
    if request.user.is_authenticated():
        count = ShopCar.objects.filter(user_id=request.user.userprofile.uid, status=1).aggregate(
            sum=Sum('book_number')).get('sum')
    return {'count': count}
