from django.urls import path
from . import views

app_name = 'marketing'
urlpatterns = [
    path('konsumen/',views.konsumen.as_view(), name='konsumen'),
    path('konsumen/<int:pk>/edit/', views.konsumenEdit.as_view(), name='konsumenEdit'),
    path('konsumen/<int:pk>/delete/', views.konsumenDelete.as_view(), name='konsumenDelete'),
    path('konsumen/<int:pk>/finish/', views.konsumenFinish.as_view(), name='konsumenFinish'),
    #path('hist_pbn/',views.hist_pbn.as_view(), name='hist_pbn'),
    #path('hist_pbn/<int:pk>/edit/', views.hist_pbnEdit.as_view(), name='hist_pbnEdit'),
    #path('hist_pbn/<int:pk>/delete/', views.hist_pbnDelete.as_view(), name='hist_pbnDelete'),
]
