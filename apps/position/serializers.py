from rest_framework import serializers
from rest_framework import routers, serializers, viewsets, permissions
from apps.position.models import Position
from django.contrib.auth import get_user_model

User = get_user_model()


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ['name', 'abbreviation']
