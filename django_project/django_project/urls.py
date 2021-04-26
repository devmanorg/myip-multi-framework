from django.urls import path

from . import views

urlpatterns = [
    path('api/ip/', views.get_my_ip, name='get_my_ip_endpoint'),
]
