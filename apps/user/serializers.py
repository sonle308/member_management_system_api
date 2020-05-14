from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework import routers, serializers, viewsets, permissions

User = get_user_model()


# # Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'avatar', 'birthday']
        username = serializers.CharField(max_length=120)
        email = serializers.EmailField(max_length=120)
        avatar = serializers.ImageField(max_length=120)
        birthday = serializers.DateTimeField()