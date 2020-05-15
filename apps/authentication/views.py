from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import serializers


@api_view(("GET",))
@permission_classes((AllowAny,))
def status_noauth(request):
    return Response({"result": "OK"})


@api_view(("GET",))
@permission_classes((IsAuthenticated,))
def status_auth(request):
    return Response({"result": "OK"})


class TokenObtainPairLoggingView(TokenObtainPairView):
    serializer_class = serializers.TokenObtainPairLoggingSerializer


class TokenRefreshLoggingView(TokenRefreshView):
    serializer_class = serializers.TokenRefreshLoggingSerializer


class AdminTokenObtainPairLoggingView(TokenObtainPairView):
    serializer_class = serializers.AdminTokenObtainPairLoggingSerializer


class AdminTokenRefreshLoggingView(TokenRefreshView):
    serializer_class = serializers.AdminTokenRefreshLoggingSerializer


token_obtain_pair = TokenObtainPairLoggingView.as_view()
token_refresh = TokenRefreshLoggingView.as_view()
admin_token_obtain_pair = AdminTokenObtainPairLoggingView.as_view()
admin_token_refresh = AdminTokenRefreshLoggingView.as_view()
