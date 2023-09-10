from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer


@api_view(["POST"])
def signup(request):    
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():                
        user = User.objects.create(username=serializer.data['email'], email=serializer.data['email'])
        user.set_password(serializer.data['password'])        
        user.save()
        
        token = Token.objects.create(user=user)

        return Response({"token": token.key}, status=status.HTTP_201_CREATED)

    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):    
    user = get_object_or_404(User, username=request.data.get('email'))
    
    if user.check_password(request.data.get('password')):
        token, created = Token.objects.get_or_create(user=user)        
        serializer = UserSerializer(user)
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(["POST"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()

    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def authenticate_with_oauth(request):
    redirect_url = request.GET.get('redirect_url')

    user = request.user
    
    token, created = Token.objects.get_or_create(user=user)        
    
    return HttpResponseRedirect(redirect_to=f"{redirect_url}?client={token.key}" )