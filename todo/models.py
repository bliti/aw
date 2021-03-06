from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Item(models.Model):
    """each specific item in a todo collection"""
    todo = models.TextField(default='...')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    #does user want to receieve a reminder alert?
    reminder = models.BooleanField(default=False)

    #datetime of alert to be sent as a reminder
    #this field is populated by data sent from template
    #through use of Jquery plugin for datetime picker.
    alert = models.DateTimeField(null=True)
        
    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-id']
    
    def __unicode__(self):
        return self.todo