from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import OrganizationSerializer
from .models import CustomUser, Organization
from django.core import serializers
from django.http import JsonResponse
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .models import Organization, CustomUser
from .serializers import OrganizationSerializer, CustomRegisterSerializer, CustomUserSerializer, CustomUserDetailsSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
# Create your views here.
# @api_view(('POST',))
# def hello(request):
#     print(request.data)
#     name = request.POST['name']
#     return Response(f"Hello {name}. Welcome to our first Flutter app.. ")


@api_view(('POST',))
def get_token(request):
    key = request.data
    token = Token.objects.filter(key=key)
    print("TOKEN IS ", token)
    return Response("get")
    # if token:
    #     user = token.user  # Access the related User object
    #     print("User is", user)
    #     return Response("User token retrieved successfully")
    # else:
    #     return Response("Token not found")


# @api_view(('POST',))
# @permission_classes([AllowAny])
# def orgsignup(request):
#     data = request.data
#     user = data['user']
#     user = CustomUser.objects.get(email=user)


#     val = {
#         'name': data['name'],
#         'user': user,
#         'address': data['address'],
#         'country': data['country'],
#         'mission': data['mission'],
#         'description': data['description'],
#         'image': data['image']
#     }
# #    user = request.user
#     print(user)
#     print(val)
#     orgdata = OrganizationSerializer(data=val)
#     # org = Organization()
#     # org.name = data['name']
#     # org.address = data['address']
#     # org.description= data['description']
#     # org.mission= data['mission']
#     # org.country= data['country']
#     # org.image= data['image']
#     # org.save()
#     print(orgdata)
#     serializers.serialize()
#     print(request.data)
#     if orgdata.is_valid():
#         orgdata.save()
#         print("SAVED")
#     else:
#         print("SOME ERROR")
#     return Response(orgdata.data)


@api_view(('POST',))
@permission_classes([AllowAny])
def orgsignup(request):
    data = request.data
    user_email = data.get('user')
    print(user_email)
    user = CustomUser.objects.get(email=user_email)
    print(user.pk)
    user = user.pk
#    user = CustomUser.objects.get_by_natural_key(user_email)

    val = {
        'name': data.get('name'),
        #    'user': user.natural_key(),
        'user': user,
        'address': data.get('address'),
        'country': data.get('country'),
        'mission': data.get('mission'),
        'description': data.get('description'),
        'image': data.get('image')
    }
    print(val)

    orgdata = OrganizationSerializer(data=val)

    if orgdata.is_valid():
        orgdata.save()
        # serialized_data = serializers.serialize(
        #     "json",
        #     [orgdata.instance],
        #     indent=2,
        #     use_natural_foreign_keys=True,
        #     use_natural_primary_keys=True,
        # )
        return Response(orgdata.data)
    else:
        return Response(orgdata.errors, status=400)


@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def organizations(request):
    if request.method == "GET":
        user = request.user
        print(user)
        org_info = Organization.objects.filter(user=user)
        print(org_info.values(), type(org_info))
        for i in org_info:
            val = {
               'name': i.name,
                #    'user': user.natural_key(),
                'user': i.user.pk,
                'address': i.address,
                'country': i.country,
                'mission': i.mission,
                'description': i.description,
                'image': i.image
               }
        print(val)

        org_info = OrganizationSerializer(data=val)
        if org_info.is_valid():
            print(org_info.data)
            print("I AM IN VALID")
            return Response(org_info.data)
        else:
            print("I HAVE ERROR")
            return Response(org_info.errors)
