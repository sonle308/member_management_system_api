from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.skill import views

app_name = 'user'

urlpatterns = [
    path('skills/', views.SkillList.as_view()),
    path('skills/<int:pk>/', views.SkillDetail.as_view()),
    path('skills/import-csv/', views.ImportCsv.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
