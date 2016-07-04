from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from autocomplete_light import shortcuts as al
al.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('webpage.urls', namespace='webpage')),
    url(r'places/', include('places.urls', namespace='places')),
    url(r'labels/', include('labels.urls', namespace='labels')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'browsing/', include('browsing.urls', namespace='browsing')),
    url(r'tablets/', include('tablets.urls', namespace='tablets')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
