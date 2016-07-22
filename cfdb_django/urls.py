from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from tablets.views import protected_serve
from autocomplete_light import shortcuts as al
from rest_framework import routers
from vocabularies.api_views import *
from tablets.api_views import *
from places.api_views import *
from labels.api_views import *
al.autodiscover()

router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet)
router.register(r'labels', LabelViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'archives', ArchiveViewSet)
router.register(r'dossiers', DossierViewSet)
router.register(r'scribes', ScribeViewSet)
router.register(r'periods', PeriodViewSet)
router.register(r'texttypes', TextTypeViewSet)
router.register(r'signs', SignViewSet)
router.register(r'tablets', TabletViewSet)
router.register(r'tabletimages', TabletImageViewSet)
router.register(r'glyphs', GlyphViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^data/api/', include(router.urls)),
    url(r'^data/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
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
