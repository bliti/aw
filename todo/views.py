from django.shortcuts import render
from django.views.generic import ListView
from models import Collection, Item


class CollectionList(ListView):
    """view all collections"""
    model = Collection
    template_name = 'todo/collection_list.html'


class ItemList(ListView):
    "view all todo items"
    model = Item
    template_name = 'todo/item_list.html'