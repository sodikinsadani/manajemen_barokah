from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'personalia'
urlpatterns = [
    path('getDataJson/',views.getDataJson.as_view(), name='getDataJson',),
    path('classBase/', views.classBase.as_view(), name='classBase'),
    path('classBase2/', views.classBase2.as_view(greeting="G'day"), name='classBase2'),
    path('classBase3/', login_required(views.classBase3.as_view()), name='classBase3'),
    path('htmlRest/', views.htmlRest.as_view(), name='htmlRest'),
    path('htmlRestAjax/', views.htmlRestAjax.as_view(), name='htmlRestAjax'),

    path('member/', views.member.as_view(), name='member'),
    path('member/<int:pk>/edit/', views.memberEdit.as_view(), name='memberEdit'),
    path('member/<int:pk>/delete/', views.memberDelete.as_view(), name='memberDelete'),
    path('laporantriwulan/', views.laporantriwulan.as_view(), name='laporantriwulan'),
]
