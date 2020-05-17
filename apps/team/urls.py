from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.team import views

app_name = 'team'

urlpatterns = [
    path('teams/', views.TeamList.as_view()),
    path('teams/<int:pk>/', views.TeamDetail.as_view()),
    path('teams/import-csv/', views.ImportCsv.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
