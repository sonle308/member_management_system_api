from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.user import views

app_name = 'user'

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/import-csv/', views.ImportCsv.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
