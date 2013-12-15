from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
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


class CollectionCreate(CreateView):
    """create a new collection"""
    model = Collection
    fields = ['name']
    template_name = 'collection_create.html'
    success_url = reverse_lazy('collection_list')


class ItemList(ListView):
    "view all todo items"
    model = Item
    template_name = 'item_list.html'


class ItemDetail(DetailView):
    """view a specific item"""
    model = Item
    template_name = "item_view.html"


class ItemCreate(CreateView):
    """create a new item"""
    model = Item
    fields = ['todo']
    template_name = 'item_create.html'
    success_url = reverse_lazy('collection_detail')

    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.collection = Collection.objects.get(id=self.kwargs['pk'])
        self.object.save()