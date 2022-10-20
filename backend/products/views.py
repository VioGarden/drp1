from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

from yaml import serialize


from .models import Product
from .serializers import ProductSerializer

# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # perhaps adding user, different serializer class (advanced for now)

#     def perform_create(self, serializer):
#         # serializer.save(user=self.request.user)
#         print(serializer.validated_data)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None
#         if content is None:
#             content = title
#         serializer.save(content=content)


# product_create_view = ProductCreateAPIView.as_view()

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # perhaps adding user, different serializer class (advanced for now)

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # loopup_field = 'pk'
product_create_view = ProductDetailAPIView.as_view()

# class ProductListAPIView(generics.ListAPIView):

#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# product_create_view = ProductListAPIView.as_view()

@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    # distinguish off of request method
    method = request.method # PUT --> update | DESTROY --> delete

    if method == "GET":
        if pk is not None: # detail view
            # getting object (not a queryset)
            # queryset = Product.objects.filter(pk=pk)
            # if queryset.exists():
            #     raise Http404
            obj = get_object_or_404(Product, pk=pk) # assume gives object (could raise 404)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # else: # list view
        queryset = Product.objects.all() # get queryset
        data = ProductSerializer(queryset, many=True).data # serializing queryset
        return Response(data)

    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # instance = serializer.save()
            # instance = form.save()
            # print(serializer.data)
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"},
        status=400)
        # create an item
