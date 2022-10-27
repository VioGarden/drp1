from rest_framework import mixins, viewsets

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    get method --> get list --> is a Queryset
    get method --> retrive item --> Product Instance Detail View
    post method --> create something --> New Instance
    put method --> update 
    patch --> partial update
    delete --> destroy
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # default

# class ProductGenericViewSet(
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     viewsets.GenericVieSet):
#     """
#     get method --> get list --> is a Queryset
#     get method --> retrive item --> Product Instance Detail View
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk' # default

# product_list_view = ProductGenericViewSet.as_view({'get': 'list'})
# product_detail_view = ProductGenericViewSet.as_view({'get': 'retrieve'})