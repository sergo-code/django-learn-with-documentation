from django.urls import path, register_converter, re_path

from .views import *
from .converters import FourDigitYearConverter


register_converter(FourDigitYearConverter, 'yyyy')
app_name = 'relationships-urls'
urlpatterns = [
    path('m2m/', relationship_m2m, name='m2m'),
    path('m2m/<yyyy:year>/', relationship_m2m),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', relationship_m2m),
]