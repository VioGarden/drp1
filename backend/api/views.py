import json # package to covert string into JSON
from django.forms.models import model_to_dict
# from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from yaml import serialize

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    # data = request.data
    # model_data = Product.objects.all().order_by("?").first()
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #     # data['id'] = model_data.id
    #     # data['title'] = model_data.title
    #     # data['content'] = model_data.content
    #     # data['price'] = model_data.price
    #     # # model instance (model_data)
    #     # # want to turn into Python Dictionary
    #     # # return JSON to client
    #     # # serialization
    #     # data = model_to_dict(model_data, fields=['id', 'title'])
    #     data = ProductSerializer(instance).data
    serializer = ProductSerializer(data=request.data) # checks if formatted correctly
    # if serializer.is_valid():
    #     print(serializer.data)
    #     data = serializer.data
    # return Response(data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save() # similar to forms.save() # cannot do commit
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "bad data"}, status=400)


# def api_home(request, *args, **kwargs):
#     # requests.body --> JSON data
#     # print(dir(request))
#     # request -> HttpRequest -> Django

#     print(request.GET) # url query params
#     print(request.POST)

#     body = request.body # byte string of JSON data
#     data = {}
#     try: # try block, for if there is no data
#         data = json.loads(body) # string of JSON data --> Python Dict
#     except:
#         pass
#     print(data)
#     # print(data.keys()) # {'message': 'Hello, this is Django API response!!'}
#     # print(body) # b'{"query": "Hello World"}' # stringified version of JSON, string around dictionary good!
#     # data['headers'] = request.headers # request.META (older version of django)
#     # print(request.headers) # cannot turn headers into JSON
#     data['params'] = dict(request.GET) # getting parameters if there is one
#     data['headers'] = dict(request.headers) # this works
#     data['content_type'] = request.content_type # in headers, but direct access
#     return JsonResponse(data)