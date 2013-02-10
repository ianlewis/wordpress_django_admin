from django.conf.urls import patterns, include, url

# Django Admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Django Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
