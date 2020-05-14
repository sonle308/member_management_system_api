import logging
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken
from apps.user.models import User

logger = logging.getLogger("event")
User = get_user_model()


class TokenObtainPairLoggingSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        logger.info(f"get api-token user={self.user.username}")

        return data


class TokenRefreshLoggingSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = RefreshToken(attrs["refresh"])
        user_id = refresh.payload["user_id"]
        user = User.objects.get(pk=user_id)
        logger.info(f"refresh api-token user={user.username}")

        return data
