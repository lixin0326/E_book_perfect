from django.db import models

# 　下单用户
from apps.comments.models import Book2


class UserProfile(models.Model):
    phone = models.CharField(max_length=11, default='15737628530')
    desc = models.CharField(max_length=255, null=True)
    uid = models.AutoField('用户ID', primary_key=True)
    user = models.OneToOneField('auth.User')

    class Meta:
        db_table = 'user_profile'
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name


# 订单
class Order(models.Model):
    ORDER_STATUS = (
        (1, '正常'),
        (0, '异常'),
        (-1, '删除'),
    )

    oid = models.AutoField('订单ID', primary_key=True)
    # 订单号唯一
    order_code = models.CharField('订单号', max_length=255)
    address = models.CharField('配送地址', max_length=255)
    post = models.CharField('邮编', max_length=255)
    receiver = models.CharField('收货人', max_length=255)
    mobile = models.CharField('手机号', max_length=11)
    user_message = models.CharField('附加信息', max_length=255)
    create_date = models.DateTimeField('创建日期', max_length=0)
    pay_date = models.DateTimeField('支付时间', max_length=0,
                                    blank=True, null=True)
    delivery_date = models.DateTimeField('交易日期', blank=True, null=True)
    confirm_date = models.DateTimeField('确认日期', blank=True, null=True)
    """ 1正常 0 异常, -1 删除 """
    status = models.IntegerField('订单状态', choices=ORDER_STATUS, default=1)
    user = models.ForeignKey('UserProfile', models.DO_NOTHING, db_column='uid', verbose_name="用户ID")

    def __str__(self):
        return self.order_code

    class Meta:
        db_table = 'order'
        verbose_name = '订单'
        verbose_name_plural = '订单管理'


# 购物车 的属性只有id 和商品数量  书名以及其他的都是Book的属性值
class ShopCar(models.Model):
    bc_id = models.AutoField(primary_key=True)
    book_number = models.IntegerField(default=0, verbose_name="商品数量")
    book = models.IntegerField(default=0, verbose_name="商品id")
    user = models.ForeignKey(UserProfile, models.DO_NOTHING, db_column='uid', verbose_name='用户ID')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, db_column='oid', null=True, verbose_name='商品ID')
    # 1正常 -1 删除 ， 禁止 2
    status = models.IntegerField(default=1)

    class Meta:
        db_table = 'shop_car'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
