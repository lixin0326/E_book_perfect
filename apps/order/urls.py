from django.conf.urls import url
from apps.order import views

urlpatterns = [

    url(r'^dingdan/', views.order, name='order'),
    url(r'^test_order/', views.test_order, name='test_order'),

]
