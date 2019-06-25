from alipay import AliPay
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from wh1804_bookstore import settings


@csrf_exempt
def pay(request):
    sumprice = request.GET.get('sumprice')
    order_code = request.GET.get('order_code')
    alipay = AliPay(
        appid=settings.APP_ID,
        # 默认回调url
        app_notify_url=None,
        alipay_public_key_path=settings.ALIPAY_PUBLIC_KEY_PATH,
        app_private_key_path=settings.APP_PRIVATE_KEY_PATH,
        sign_type='RSA2',
        debug=True,
    )
    order_url = alipay.api_alipay_trade_page_pay(
        subject='鑫宝来',
        out_trade_no=order_code,
        total_amount=sumprice,
        # 支付成功跳转的页面
        return_url='http://127.0.0.1:8688/'
    )
    pay_url = settings.ALI_PAY_DEV_URL + "?" + order_url
    return redirect(pay_url)
