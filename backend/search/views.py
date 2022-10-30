from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer

class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # want to verify what we're looking up is public

    def get_queryset(self, *args, **kwargs):
        # calling default value of queryset
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        results = Product.objects.none() # by default, results are none
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results