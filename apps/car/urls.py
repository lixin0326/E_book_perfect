from django.conf.urls import url

from apps.car import views

urlpatterns = [
    url('add/', views.add, name='add'),
    url('delete/', views.delete, name='delete'),
    url('update/', views.update_num, name='update'),
    url('list_result/', views.list_result, name='list_result'),

]
