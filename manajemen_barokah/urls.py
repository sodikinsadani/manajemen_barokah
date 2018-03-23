from django.contrib import admin
from django.urls import path,include

from homepage import views as homepage_views
from karyawan import views as karyawan_views
from enterprise import views as enterprise_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', enterprise_views.index.as_view(), name='index'),
    path('login/', homepage_views.login_view, name='login'),
    path('logout/', homepage_views.logout_view, name='logout'),
    path('marketing/', include('marketing.urls')),
    path('training/', include('training.urls')),
    path('ekonomi/', include('ekonomi.urls')),
    path('personalia/', include('personalia.urls')),
    path('enterprise/', include('enterprise.urls')),
    #url('api-auth/', include('rest_framework.urls'))
]
