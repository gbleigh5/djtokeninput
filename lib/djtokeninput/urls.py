#!/usr/bin/env python

from django.conf.urls import url, include
from .views import search


urlpatterns = [
  url(r"^(?P<app_label>\w+)/(?P<model>\w+)$", search, name="djtokeninput_search")
]
