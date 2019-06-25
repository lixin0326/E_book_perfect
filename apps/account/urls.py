from django.conf.urls import url

from apps.account import userhelper
from apps.account import views

urlpatterns = [
    url('login/', views.login_view, name='login'),
    url('register/', views.register_view, name='register'),
    url('login_out/', views.logout_view, name='login_out'),
    url('active/', views.ActivateHandler),
]
