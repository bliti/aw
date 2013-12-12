from django.conf.urls.defaults import patterns, url
from todo.views import CollectionList, ItemList


urlpatterns = patterns('todo.views',
    url(r'^collections/$', CollectionList.as_view()),
    url(r'^items/$', CollectionList.as_view()),
    )