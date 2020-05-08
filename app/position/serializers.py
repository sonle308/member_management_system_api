from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import routers, serializers, viewsets, permissions
from app.user.models import Position


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ['name', 'abbreviation']