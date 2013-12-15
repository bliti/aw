from django.db import models


class Collection(models.Model):
    """Collection of todo items."""
    name = models.TextField(default='Blank!')
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:

        ordering = ['-id']


    def __unicode__(self):
        return str(self.id)


class Item(models.Model):
    """each specific item in a todo collection"""
    todo = models.TextField(default='...')
    created_at = models.DateTimeField(auto_now_add=True)
    collection = models.ForeignKey('Collection')


    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.todo