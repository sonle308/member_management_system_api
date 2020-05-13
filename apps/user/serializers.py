from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import routers, serializers, viewsets, permissions


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']



