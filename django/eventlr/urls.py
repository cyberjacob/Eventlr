from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'web.pages.index', name='home'),
    # url(r'^eventlr/', include('eventlr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^my-admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^my-admin/', include(admin.site.urls)),

    url(r'^account/', include('registration.backends.default.urls')),
)
