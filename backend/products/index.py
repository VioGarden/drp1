from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    # should_index = 'is_public'
    fields = [
        'title',
        'body',# 'content',
        'price',
        'user',
        'public',
        #'password', Nope
        #'customer-email', Nope
        'path',
        'endpoint',
    ]
    settings = {
        # 'searchableAttributes': ['title', 'content'],
        'searchableAttributes': ['title', 'body'],
        'attributesForFaceting': ['user', 'public'],
    }
    tags = 'get_tags_list'

# similar to admin.site.register(Product, ProductModelAdmin)