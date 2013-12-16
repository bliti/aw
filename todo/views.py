from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from models import Collection, Item


def home(request):
    return render(request, 'index.html')


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


class CollectionDelete(DeleteView):
    """delete a collection"""
    model = Collection
    success_url = reverse_lazy('collection_list')
    template_name = 'collection_confirm_delete.html'


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
    
    
    def form_valid(self, form):
        #get the foreign key collection object
        form.instance.collection = get_object_or_404(Collection,id=self.kwargs['pk'])
        return super(ItemCreate, self).form_valid(form)


class ItemDelete(DeleteView):
    """delete an item"""
    model = Item
    template_name = 'item_confirm_delete.html'
    

    def get_success_url(self, **kwargs):
        return reverse_lazy('collection_detail', kwargs={'pk': self.collection_pk})
    
    def delete(self, request, *args, **kwargs):
        #get pk of collection item belonged to
        self.collection_pk = self.get_object().collection.pk
        return super(ItemDelete, self).delete(request, *args, **kwargs)