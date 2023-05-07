from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(('POST',))
def hello(request):
    print(request.data)
    name = request.POST['name']
    return Response(f"Hello {name}. Welcome to our first Flutter app.. ")