from django.urls import include, path
from rest_framework import routers
from apps.user import views

router = routers.DefaultRouter()
router.register(r'api/v1/users/', views.UserList, basename='User')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api/v1/", include("apps.authentication.urls")),
    path("api/v1/", include("apps.user.urls")),
    path("api/v1/", include("apps.skill.urls")),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls
