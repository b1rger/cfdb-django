from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from tablets.views import protected_serve

from autocomplete_light import shortcuts as al

al.autodiscover()
#url(r'^edit/(?P<pk>[0-9]+)$', views.edit_tablet, name='tablet_edit'),

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('webpage.urls', namespace='webpage')),
    url(r'^media/tablet_img/(?P<pic>.*)$', protected_serve, name='protected_server'),
    url(r'places/', include('places.urls', namespace='places')),
    url(r'labels/', include('labels.urls', namespace='labels')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'browsing/', include('browsing.urls', namespace='browsing')),
    url(r'tablets/', include('tablets.urls', namespace='tablets')),
    url(r'charts/', include('charts.urls', namespace='charts')),
    url(r'^datamodel/', include('django_spaghetti.urls', namespace='datamodel')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
