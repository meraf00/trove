from rest_framework import serializers
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=5, max_length=20, allow_blank=False, required=True)
    first_name = serializers.CharField(allow_blank=True, required=False, default='')
    last_name = serializers.CharField(allow_blank=True, required=False, default='')

    class Meta:
        model = User
        fields = ('username', 'email',  'password', 'first_name', 'last_name')


class AuthSerializer(serializers.ModelSerializer):
    username = serializers.CharField(allow_blank=True, required=False, default='')
    email = serializers.CharField(allow_blank=True, required=False, default='')

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
    def validate(self, attrs):
        if not attrs.get('username') and not attrs.get('email'):
            raise serializers.ValidationError({"user" : "Please provide username or email."})
        return attrs