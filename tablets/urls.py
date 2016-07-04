from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^detail/(?P<pk>[0-9]+)$', views.TabletDetailView.as_view(), name='tablet_detail'),
    url(r'^create/$', views.create_tablet, name='tablet_create'),
    url(r'^edit/(?P<pk>[0-9]+)$', views.edit_tablet, name='tablet_edit'),
    url(r'^sign/detail/(?P<pk>[0-9]+)$', views.SignDetailView.as_view(), name='sign_detail'),
    url(r'^sign/create/$', views.create_sign, name='sign_create'),
    url(r'^sign/edit/(?P<pk>[0-9]+)$', views.edit_sign, name='sign_edit'),
    url(r'^glyph/detail/(?P<pk>[0-9]+)$', views.GlyphDetailView.as_view(), name='glyph_detail'),
    url(r'^glyph/create/$', views.create_glyph, name='glyph_create'),
    url(r'^glyph/edit/(?P<pk>[0-9]+)$', views.edit_glyph, name='glyph_edit'),
    url(r'^tabletImg/detail/(?P<pk>[0-9]+)$',
        views.TabletImageDetailView.as_view(), name='tabletImg_detail'),
    url(r'^tabletImg/create/$', views.create_tabletImg, name='tabletImg_create'),
    url(r'^tabletImg/edit/(?P<pk>[0-9]+)$', views.edit_tabletImg, name='tabletImg_edit'),
]
