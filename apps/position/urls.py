from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.position import views

app_name = 'position'

urlpatterns = [
    path('positions/', views.PositionList.as_view()),
    path('positions/<int:pk>/', views.PositionDetail.as_view()),
    path('positions/import-csv/', views.ImportCsv.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
