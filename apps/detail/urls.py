from django.conf.urls import url

from apps.detail import views

urlpatterns = [
    url('showDetail/', views.detail, name='showDetail'),

]
