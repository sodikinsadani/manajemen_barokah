from django.urls import path
from . import views

app_name = 'ekonomi'
urlpatterns = [
    path('insod/', views.insod.as_view(), name='insod'),
    path('insod/<int:pk>/edit/', views.insodEdit.as_view(), name='insodEdit'),
    path('insod/<int:pk>/delete/', views.insodDelete.as_view(), name='insodDelete'),
]
