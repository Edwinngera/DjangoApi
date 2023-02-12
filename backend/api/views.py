from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer




# Create your views here.
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """DRF API View"""
    model_data=Product.objects.all().order_by('?').first();
    data={}
    # if model_data:
    #     data["title"]=model_data.title
    #     data["content"]=model_data.content
    #     data["price"]=model_data.price
    if model_data:
        data=model_to_dict(model_data,fields=['id', 'title','price'])
    return Response(data)

#Test Serializers
@api_view(["GET"])
def api_test(request, *args, **kwargs):
    instance=Product.objects.all().order_by("?").first()
    data={}
    if instance:
        data=ProductSerializer(instance).data
    return Response(data)

@api_view(["POST"])
def api_create(request, *args, **kwargs):
    data=request.data
    serializer=ProductSerializer(data=data)
    if serializer.is_valid():
        print(serializer.data)
        data=serializer.data
    return Response(data)



  

