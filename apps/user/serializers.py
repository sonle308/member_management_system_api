from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework import routers, serializers, viewsets, permissions

User = get_user_model()

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']



