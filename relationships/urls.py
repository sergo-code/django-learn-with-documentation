from django.urls import path, register_converter, re_path

from .views import *
from .converters import FourDigitYearConverter


register_converter(FourDigitYearConverter, 'yyyy')
app_name = 'relationships-urls'
urlpatterns = [
    path('', get_name),
    path('reverse-form/', reverse_form),
    path('thanks/', thanks),
    path('index/', index),
    path('smart/', smart_func),
    path('vk-page/', hardcoded_URL),
    path('m2m/', relationship_m2m, name='m2m'),
    path('m2m/<yyyy:year>/', relationship_m2m),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', relationship_m2m),
]