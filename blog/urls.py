from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('post/<int:id>/', views.post, name='post'),
    path('create_post/', views.create_post, name='create_post'),
]
