from django.urls import path
from . import views

app_name = 'ekonomi'
urlpatterns = [
    path('insod/', views.insod.as_view(), name='insod'),
    path('insod/<int:pk>/edit/', views.insodEdit.as_view(), name='insodEdit'),
    path('insod/<int:pk>/delete/', views.insodDelete.as_view(), name='insodDelete'),
    path('kue/', views.kue.as_view(), name='kue'),
    path('kue/<int:pk>/edit/', views.kueEdit.as_view(), name='kueEdit'),
    path('kue/<int:pk>/delete/', views.kueDelete.as_view(), name='kueDelete'),
    path('penjualankue/', views.penjualanKue.as_view(), name='penjualankue'),
    path('penjualankue/<int:pk>/edit/', views.penjualankueEdit.as_view(), name='penjualankueEdit'),
    path('penjualankue/<int:pk>/delete/', views.penjualankueDelete.as_view(), name='penjualankueDelete'),
    path('pengambilankuesales/', views.pengambilankuesalesKue.as_view(), name='pengambilankuesales'),
    path('pengambilankuesales/<int:pk>/edit/', views.pengambilankuesalesEdit.as_view(), name='pengambilankuesalesEdit'),
    path('pengambilankuesales/<int:pk>/delete/', views.pengambilankuesalesDelete.as_view(), name='pengambilankuesalesDelete'),
    path('pengambilankueagen/', views.pengambilankueagen.as_view(), name='pengambilankueagen'),
]
