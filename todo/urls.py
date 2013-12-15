from django.conf.urls import patterns, url
from todo.views import CollectionList, ItemList, CollectionDetail, ItemDetail


urlpatterns = patterns('todo.views',
    url(r'^collections/$', CollectionList.as_view(), name="collections"),
    url(r'^items/$', ItemList.as_view(), name="items"),
    url(r'^collection/(?P<pk>\w+)/$',
        CollectionDetail.as_view(), 
        name="collection_detail"),
    url(r'^item/(?P<pk>\w+)/$',
        ItemDetail.as_view(), 
        name="item_detail"),    
    )