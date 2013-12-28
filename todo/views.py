from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from models import Item


class ItemList(ListView):
    "view all todo items"
    model = Item
    template_name = 'item_list.html'


    def get_queryset(self):
        return get_object_or_404(User, id=self.request.user.id).item_set.all() 


class ItemDetail(DetailView):
    """view a specific item"""
    model = Item
    template_name = "item_view.html"


    def get_object(self, queryset=None):
        object = super(ItemDetail, self).get_object(queryset)
        if object.user_id != self.request.user.id:
            raise Http404
        return object
        
        
class ItemCreate(CreateView):
    """create a new item"""
    model = Item
    fields = ['todo']
    template_name = 'item_create.html'
    success_url = reverse_lazy('item_list')
    
    
    def form_valid(self, form):
        #get the foreign key collection object
        form.instance.user = get_object_or_404(User, id=self.request.user.id)
        return super(ItemCreate, self).form_valid(form)
    
    
    #def form_valid(self, form):
        #get the foreign key collection object
    #    form.instance.collection = get_object_or_404(Collection,id=self.kwargs['pk'])
    #    return super(ItemCreate, self).form_valid(form)


class ItemDelete(DeleteView):
    """delete an item"""
    model = Item
    template_name = 'item_confirm_delete.html'
    success_url = reverse_lazy('item_list')
    

    #def get_success_url(self, **kwargs):
    #    return reverse_lazy('collection_detail', kwargs={'pk': self.collection_pk})
    
    #def delete(self, request, *args, **kwargs):
    #    #get pk of collection item belonged to
    #    self.collection_pk = self.get_object().collection.pk
    #    return super(ItemDelete, self).delete(request, *args, **kwargs)