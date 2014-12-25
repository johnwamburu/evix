from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'evix.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'evix.views.index', name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
