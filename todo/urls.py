from django.conf.urls import patterns, url
from todo.views import CollectionList, ItemList, CollectionDetail, ItemDetail,\
                       CollectionCreate, ItemCreate


urlpatterns = patterns('todo.views',
    url(r'^collections/$', CollectionList.as_view(), name="collection_list"),
    #
    url(r'^items/$', ItemList.as_view(), name="item_list"),
    #
    url(r'^collection/(?P<pk>\w+)/item/new/$',
        ItemCreate.as_view(), 
        name="item_create"),    
    #
    url(r'^collection/new/$',
        CollectionCreate.as_view(),
        name="collection_create"),
    #
    url(r'^collection/(?P<pk>\w+)/$',
        CollectionDetail.as_view(), 
        name="collection_detail"),
    #
    url(r'^item/(?P<pk>\w+)/$',
        ItemDetail.as_view(), 
        name="item_detail"), 
    )