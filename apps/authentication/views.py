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


token_obtain_pair = TokenObtainPairLoggingView.as_view()
token_refresh = TokenRefreshLoggingView.as_view()
