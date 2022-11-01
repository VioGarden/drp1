# from re import L
import random
from django.db import models
from django.conf import settings

from django.db.models import Q

User = settings.AUTH_USER_MODEL # auth.User string

TAGS_MODEL_VALUES = ['electronics', 'cars', 'movies', 'boats', 'cameras']

class ProductQuerySet(models.QuerySet): # custom queryset
    def is_public(self): 
        return self.filter(public=True)

    def search(self, query, user=None): 
        # lookup looks in title and content fields, for a match, then filter further based on user
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None: # filter further
            qs2 = self.filter(user=user).filter(lookup) # doesn't matter if public or not
            results = (qs | qs2).distinct()
        return results

class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs): # overriding default, so args, kwarhs
        return ProductQuerySet(self.model, using=self.db) # self._db, default database

    def search(self, query, user=None): # takes in query and user potentially
        return self.get_queryset().search(query, user=user)

# Create your models here.
class Product(models.Model):
    # owner = models.ForeignKey(User) for custom permissions
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15,
    decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)
    
    objects = ProductManager()

    def is_public(self):
        return self.public # True of False

    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]

    def get_absolute_url(self):
        return f"/api/products/{self.pk}/"

    @property
    def endpoint(self):
        return self.get_absolute_url()

    @property
    def path(self):
        return f"/products/{self.pk}/"

    @property
    def sale_price(self):
        return "%.2f"%(float(self.price)*0.8)

    def get_discount(self):
        return "Discount!!!"
    
    def body(self):
        return self.content