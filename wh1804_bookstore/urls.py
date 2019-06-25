from django.conf.urls import url, include
from django.contrib import admin
import xadmin
from apps.home import views

urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    url('^$', views.home),
    url('home/', include('apps.home.urls')),
    url('detail/', include('apps.detail.urls')),
    url('account/', include('apps.account.urls')),
    url('car/', include('apps.car.urls')),
    url('order/', include('apps.order.urls')),
    url('search/', include('apps.search.urls')),
    url('comments/', include('apps.comments.urls')),
    url('drf_apis/', include('apps.drf_apis.urls')),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url('pay/', include('apps.pay.urls')),
]
