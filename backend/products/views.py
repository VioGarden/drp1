from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

from yaml import serialize

# from api.authentication import TokenAuthentication

from api.mixins import StaffEditorPermissionMixin

from .models import Product
# from ..api.permissions import IsStaffEditorPermissions
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

class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # perhaps adding user, different serializer class (advanced for now)
    # authentication_classes = [
        # authentication.SessionAuthentication,
        # authentication.TokenAuthentication,
        # TokenAuthentication
        # ]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]
    # loopup_field = 'pk'
product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]
    loopup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save() # identical to perform_create instance
        if not instance.content:
            instance.content = instance.title
            
product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    loopup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)
            
product_destroy_view = ProductDestroyAPIView.as_view()

# class ProductListAPIView(generics.ListAPIView):

#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# product_create_view = ProductListAPIView.as_view()

class CreateAPIView(mixins.CreateModelMixin, generics.GenericAPIView): # create API view
    pass

class ProductMixinView(
    # unpacking following four into one single view
    mixins.CreateModelMixin,
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin, # for lookup_field, cares about look_up field
    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # only matters for things it matters to
    def get(self, request, *args, **kwargs):
        print(args, kwargs) # shows up in terminal
        pk = kwargs.get("pk")
        if pk is not None: 
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs): #HTTP --> Post # when use mixins, access to methods in mixin
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is hehe"
        serializer.save(content=content)

product_mixin_view = ProductMixinView.as_view()

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
