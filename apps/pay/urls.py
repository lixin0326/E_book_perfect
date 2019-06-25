from django.conf.urls import url

from apps.pay import views

urlpatterns = [
    url('ali_pay/', views.pay, name='pay'),
]
