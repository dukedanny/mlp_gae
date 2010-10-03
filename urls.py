from django.conf.urls.defaults import *
import os.path

static = os.path.join(
                          os.path.dirname(__file__),
                          'static/stylesheets/'
                          )
urlpatterns = patterns('',
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
    ('^login/$', 'django.contrib.auth.views.login'),
    ('^logout/$', 'django.contrib.auth.views.logout'),
    (r'^site_media/(?P<path>.*)$','django.views.static.serve',
     {'document_root':static}),
)
