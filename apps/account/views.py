import uuid
from django.core.cache import cache
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from apps.account import tasks
from wh1804_bookstore import settings


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("登录失败!")


# 登出操作
def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        # 刚开始注册不激活,需要邮箱来激活!
        is_active = 0
        user = User.objects.filter(username=username)
        if password != password2:
            return HttpResponse("两次密码不一致,请重新注册!")

        if user:
            return HttpResponse('该用户已经存在!')
        else:
            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=email,
                                            is_active=is_active)
            user.save()

            try:
                token = str(uuid.uuid4())

                cache.set(token, user.pk, timeout=2 * 60 * 60 * 24)

                active_url = "http://%s:%s/account/active/?token=%s" % (settings.DJANGO_SERVICE[0],
                                                                        settings.DJANGO_SERVICE[1],
                                                                        token)

                receive_mail = email

                tasks.delay_send_mail.delay(username, active_url, receive_mail, "注册邮箱激活")

            except Exception as e:
                print(e)

        return redirect("/account/login/")


def ActivateHandler(request):
    token = request.GET.get('token')
    user_id = cache.get(token)

    if user_id:
        cache.delete(token)
        user = User.objects.get(pk=user_id)
        user.is_active = 1
        user.save(update_fields=['is_active'])

        return HttpResponse(f"用户{user.username} 激活成功")
    else:
        return HttpResponse("激活用户信息过期，请重新申请激活邮件")
