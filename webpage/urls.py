from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<template>\w*)$', views.template_view, name="template"),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^accounts/login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
]
