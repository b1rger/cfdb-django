from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'tablets/$', views.TabletListView.as_view(), name='browse_tablets'),
    url(r'signs/$', views.SignListView.as_view(), name='browse_signs'),
    url(r'glyphs/$', views.GlyphListView.as_view(), name='browse_glyphs'),
    url(r'tabletimages/$', views.TabletImageListView.as_view(), name='browse_tabletimages'),
]
