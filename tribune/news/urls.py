from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^today/$',views.newsOfTheDay,name='newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.pastDaysNews,name='pastNews')
]
