#coding:utf-8
import sae

from lab3byjiafei import wsgi

application = sae.create_wsgi_app(wsgi.application)
