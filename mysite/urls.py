from django.conf.urls.defaults import *
from django.conf import settings
from django.shortcuts import redirect
import os.path

PWD = os.path.dirname(os.path.realpath(__file__ )) 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', lambda x: redirect('/blog')),
    (r'^blog/$', 'blog.views.index'),
    (r'^contact/', 'blog.views.contact'),
    (r'^about/', 'blog.views.about'),
    (r'^members/', 'tadkamembers.views.memberpage'),
    (r'^music/','setlist.views.music'),
    #(r'^blog/(?P<blog_id>\d+)/$', 'blog.views.detail'),
    #(r'^blog/(?P<blog_id>\d+)/post/$', 'blog.views.post'),
    (r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(PWD,'../site_media/')}),
    )

