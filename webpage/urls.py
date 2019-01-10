from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'webpage'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?!admin)(?P<template>\w*)$', views.template_view, name="template"),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^accounts/login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
     url(r'^project-info/$', views.project_info, name='project_info'),
]
