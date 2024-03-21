from django.urls import path
from . import views

urlpatterns = [
    path('getUser', views.get_data),
    path('register', views.create_user),
    path('login', views.authenticate_user)
]