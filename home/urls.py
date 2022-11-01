from django.urls import path
from home import views, api

urlpatterns = [
    path('', views.home, name='home'),
    path('api/bg-home', api.bg_home, name='bg-home'),
]
