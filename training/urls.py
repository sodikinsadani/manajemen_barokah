from django.urls import path
from . import views

app_name = 'training'
urlpatterns = [
    path('peserta/',views.peserta.as_view(), name='peserta'),
    path('peserta/<int:pk>/edit/', views.pesertaEdit.as_view(), name='pesertaEdit'),
    path('peserta/<int:pk>/delete/', views.pesertaDelete.as_view(), name='pesertaDelete'),
    path('hist_pbn/',views.hist_pbn.as_view(), name='hist_pbn'),
    path('hist_pbn/<int:pk>/edit/', views.hist_pbnEdit.as_view(), name='hist_pbnEdit'),
    path('hist_pbn/<int:pk>/delete/', views.hist_pbnDelete.as_view(), name='hist_pbnDelete'),
]
