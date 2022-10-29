from rest_framework import serializers
# import could create looped imports and nested imports, not good
class UserProductInlineSerializer(serializers.Serializer):
    # in theory serializers user.product_set.all()
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True) # prob most practical
    id = serializers.IntegerField(read_only=True) # prob most practical
    # other_products = serializers.SerializerMethodField(read_only=True)
    # # nested, nested serializer, not practical, but shows how to bring in nested data 
    # def get_other_products(self, obj): 
    #     # request = self.context.get('request')
    #     # print(obj)
    #     user = obj
    #     # my_products = user.product_set.all()
    #     my_products_qs = user.product_set.all()[:5] # prob not the best practice
    #     return UserProductInlineSerializer(my_products_qs, many=True, context=self.context).data