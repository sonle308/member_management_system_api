from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import viewsets

from app.user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
