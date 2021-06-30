from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.main_redirect_view),
    path('home/', views.main_view, name="home"),

    path('api/', include('applications.API.urls', namespace="api")),
]
