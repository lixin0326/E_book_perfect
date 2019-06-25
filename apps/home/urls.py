from django.conf.urls import url
from apps.home import views

urlpatterns = [
    url('guide/', views.book_guide, name='guide'),
    url('cat_home/', views.cat_home, name='cat_home'),

]
