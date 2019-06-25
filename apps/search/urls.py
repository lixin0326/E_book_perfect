from django.conf.urls import url

from apps.search import views

urlpatterns = [
    url('result_list/', views.search, name='search'),
]
