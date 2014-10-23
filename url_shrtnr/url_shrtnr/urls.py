from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'url_shrtnr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','url_short.views.home'),
    url(r'^(?P<url>[-a-zA-Z0-9]+)/?$', 'url_short.views.change'),
)
