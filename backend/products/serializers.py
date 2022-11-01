from wsgiref.validate import validator
from requests import request
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title
from .validators import validate_title_no_hello, unique_product_title
from api.serializers import UserPublicSerializer

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    # my_user_data = serializers.SerializerMethodField(read_only=True) # not idea 1
    # my_discount = serializers.SerializerMethodField(read_only=True)
    # user = UserPublicSerializer(read_only=True)
    owner = UserPublicSerializer(source='user', read_only=True)
    # related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk')
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
    # name = serializers.CharField(source='title', read_only=True)
    # email = serializers.EmailField(write_only=True)
    # email = serializers.CharField(source='user.email', write_only=True)
    body = serializers.CharField(source='content')
    class Meta:
        model = Product
        fields = [
            # 'user',
            'owner',
            'url',
            'edit_url',
            'pk',
            # 'email',
            # 'name',
            'title',
            # 'content',
            'body',
            'price',
            'sale_price',
            'public',
            # 'my_discount',
            # 'related_products',
            'path',
            'endpoint',
        ]
    # def get_my_user_data(self, obj): # not ideal 1
    #     return {
    #         "username": obj.user.username
    #     }

    # def validate_title(self, value):
    #     # look a queryset up in the database, if title exists somewhere
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value

    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data) # by default
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title')
    #     return instance # saves by default

    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)

    # def get_url(self, obj): # wrong way to url
        # return f"/api/products/{obj.pk}/" # wrong way to url

    # def get_url(self, obj):
    #     request = self.context.get('request') # serializers dont always have request
    #     if request is None:
    #         return None
    #     # reversing ('<int:pk>/', views.product_detail_view, name='product-detail'),
    #     # pk is keyword argument (kwarg)
    #     return reverse("product-detail", kwargs={"pk": obj.ok}, request=request)

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    # def get_my_discount(self, obj):
    #     # try:
    #     #     return obj.get_discount()
    #     # except:
    #     #     return None
    #     if not hasattr(obj, 'id'): # checking data for instance
    #         return None
    #     if not isinstance(obj, Product): # checking data for instance
    #         return None
    #     return obj.get_discount()
            