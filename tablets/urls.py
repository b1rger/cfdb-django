from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^detail/(?P<pk>[0-9]+)$', views.TabletDetailView.as_view(), name='tablet_detail'),
    url(r'^detail/(?P<pk>[0-9]+)/xml$', views.tablet_to_tei, name='tablet_to_tei'),
    url(r'^create/$', views.create_tablet, name='tablet_create'),
    url(r'^edit/(?P<pk>[0-9]+)$', views.edit_tablet, name='tablet_edit'),
    url(r'^delete/(?P<pk>[0-9]+)$', views.TabletDelete.as_view(), name='tablet_delete'),
    url(r'^sign/detail/(?P<pk>[0-9]+)$', views.SignDetailView.as_view(), name='sign_detail'),
    url(r'^sign/create/$', views.create_sign, name='sign_create'),
    url(r'^sign/edit/(?P<pk>[0-9]+)$', views.edit_sign, name='sign_edit'),
    url(r'^sign/delete/(?P<pk>[0-9]+)$', views.SignDelete.as_view(), name='sign_delete'),
    url(r'^glyph/detail/(?P<pk>[0-9]+)$', views.GlyphDetailView.as_view(), name='glyph_detail'),
    url(r'^glyph/create/$', views.create_glyph, name='glyph_create'),
    url(r'^glyph/edit/(?P<pk>[0-9]+)$', views.edit_glyph, name='glyph_edit'),
    url(r'^glyph/delete/(?P<pk>[0-9]+)$', views.GlyphDelete.as_view(), name='glyph_delete'),
    url(r'^tabletimg/detail/(?P<pk>[0-9]+)$',
        views.TabletImageDetailView.as_view(), name='tabletimg_detail'),
    url(r'^tabletimg/create/$', views.create_tabletImg, name='tabletimg_create'),
    url(r'^tabletimg/edit/(?P<pk>[0-9]+)$', views.edit_tabletImg, name='tabletimg_edit'),
    url(
        r'^tabletimage/delete/(?P<pk>[0-9]+)$',
        views.TabletImageDelete.as_view(), name='tabletimage_delete'),
    url(
        r'^tabletimage/cut/(?P<pk>[0-9]+)$',
        views.cut_tabletImg, name='tabletimage_cut'),
]
