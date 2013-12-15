from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from models import Collection, Item


class CollectionList(ListView):
    """view all collections"""
    model = Collection
    template_name = 'collection_list.html'


class CollectionDetail(DetailView):
    """view a specific collection"""
    model = Collection
    template_name = 'collection_view.html'


    def get_queryset(self):
        """return all related items to a collection"""
        return get_object_or_404(Collection,id=self.kwargs['pk']).item_set.all()


class ItemList(ListView):
    "view all todo items"
    model = Item
    template_name = 'item_list.html'


class ItemDetail(DetailView):
    """view a specific item"""
    model = Item
    template_name = "item_view.html"