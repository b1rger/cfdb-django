from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^barcharts/$', views.barcharts_view, name='bar_charts'),
    url(r'^testjson/$', views.test_json, name='test_json'),
    url(r'^tablets_per_region/$', views.tablets_per_region, name='tablets_per_region'),
    url(r'^tablets_per_scribe/$', views.tablets_per_scribe, name='tablets_per_scribe'),
    url(r'^tablets_per_period/$', views.tablets_per_period, name='tablets_per_period'),
    url(r'^glyphs_per_sign/$', views.glyphs_per_sign, name='glyphs_per_sign'),
]
