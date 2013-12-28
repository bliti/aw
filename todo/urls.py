from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from todo.views import ItemDelete, ItemCreate, ItemList, ItemDetail


urlpatterns = patterns('todo.views',
    #
    url(r'^item/all/$', login_required(ItemList.as_view()), name="item_list"),   
    #
    url(r'^item/new/$',
        login_required(ItemCreate.as_view()), 
        name="item_create"),
    #
    url(r'^item/(?P<pk>\w+)/$',
        login_required(ItemDetail.as_view()), 
        name="item_detail"), 
    #
    url(r'^item/delete/(?P<pk>\w+)/$',
        login_required(ItemDelete.as_view()), 
        name="item_delete"),
    )