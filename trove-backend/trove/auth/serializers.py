from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'date_joined')


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')