from django.urls import path
from . import views

app_name = 'training'
urlpatterns = [
    path('peserta/',views.peserta.as_view(), name='peserta'),
    path('peserta/<int:pk>/edit/', views.pesertaEdit.as_view(), name='pesertaEdit'),
    #path('peserta/<int:pk>/delete/', views.pesertaDelete.as_view(), name='pesertaDelete'),
]
