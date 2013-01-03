from django.conf.urls import patterns, include, url
from django.conf import settings

import os
here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pmh_images.views.home', name='home'),
    # url(r'^pmh_img/', include('pmh_img.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

#hacky, but this should be a low-volume site
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': here('../media')}),
    )
