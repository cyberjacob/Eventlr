from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'web.pages.index', name='home'),
    #url(r'^api/', include('api.urls')),
    # url(r'^eventlr/', include('eventlr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^account/', include('registration.backends.default.urls')),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace = 'oauth2')),

    url(r'^legal/terms$', 'direct_to_template', {'template': 'terms.html'}),
    url(r'^legal/privacy$', 'direct_to_template', {'template': 'privacy.html'}),
)
