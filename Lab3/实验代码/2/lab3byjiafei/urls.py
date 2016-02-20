# -*- coding: utf-8 -*-
"""Lab3byjiafei URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from bookmanager import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^option/$', views.Option, name = 'option'),
    url(r'^addbook/$', views.Addbook, name = 'addbook'),
    url(r'^updatebook/(?P<book_pk>\d+)/$', views.Updatebook, name = 'updatebook'),
    url(r'^addauthor/$', views.Addauthor, name = 'addauthor'),
    url(r'^checkauthorID/$', views.CheckauthorID, name = 'checkauthorID'),
    url(r'^search/$', views.Search, name = 'search'),
    url(r'^detail/(?P<book_pk>\d+)/$', views.Detail, name = 'detail'),
    url(r'^delete/(?P<book_pk>\d+)/(?P<author_pk>\d+)/$', views.Delete, name = 'delete'),
]
