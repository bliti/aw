from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #
    #this line redirects users after registration is successful
    #to the view where their list of items is displayed
    #url(r'^users/(?P<pk>\w+)/$', RedirectView.as_view(url=reverse_lazy('item_list'))),
    #
    #
    #url(r'^', include('todo.urls')),
    (r'^accounts/', include('registration.backends.simple.urls')),
    )