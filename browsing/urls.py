from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'tablets/$', views.TabletsListView.as_view(), name='browse_tablets'),
]
