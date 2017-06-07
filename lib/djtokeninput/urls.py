#!/usr/bin/env python

from django.conf.urls import url, include


urlpatterns = [
  url(r"^(?P<app_label>\w+)/(?P<model>\w+)$", "djtokeninput.views.search", name="djtokeninput_search")
]
