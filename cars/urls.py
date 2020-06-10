from django.urls import path
from django.conf.urls import url
from .views import car_list, car_detail, search

app_name = 'cars'
urlpatterns = [
    url(r'^car-list/$', car_list, name='car-list'),
    url(r'^results/$', search, name='search'),
    url(r'car-detail/(?P<slug>[-w]+)/$', car_detail, name='car-detail'),
    # url(r'^results/$', search, name='search'),
]
