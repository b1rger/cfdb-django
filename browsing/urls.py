from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'tablets/$', views.TabletListView.as_view(), name='browse_tablets'),
    url(r'signs/$', views.SignListView.as_view(), name='browse_signs'),
]
