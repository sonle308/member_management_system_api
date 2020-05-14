from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'auth'

# router = DefaultRouter()

# urlpatterns = [
    
# ]

router = DefaultRouter()

# apiurlpatterns = router.urls

urlpatterns = [
    path(
        "api-token/", views.token_obtain_pair, name="token_obtain_pair",
    ),
    path(
        "api-token/refresh/", views.token_refresh, name="token_refresh",
    ),
]
