from django.conf.urls import patterns, include, url
from website.views import AWRegistrationView


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^todo/', include('todo.urls')),
    url(r'^$', include('website.urls')),
    # custom registration view
    url(r'^register/$', AWRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)
