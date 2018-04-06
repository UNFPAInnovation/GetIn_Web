from django.conf import settings
from django.conf.urls import patterns, url, include
#from django.views.generic.simple import redirect_to

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'mds.clients.views.version', name="android"),
    url(r'^download/$', 'mds.clients.views.download_latest'),
    url(r'^report/submit/$', 'mds.clients.views.submit_crash'),
    )