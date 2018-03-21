from django.urls import path
from . import views

app_name = 'enterprise'
urlpatterns = [
    path('report/', views.report.as_view(), name='report'),
    path('reportdownload/<int:pk>/', views.reportdownload.as_view(), name='reportdownload'),
    path('getDataChart/', views.getDataChart.as_view(), name='getDataChart'),
]
