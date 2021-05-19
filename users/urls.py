from django.urls import path, include
from rest_framework.settings import import_from_string
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('all-profiles', UsersProfileListAPIView.as_view(), name='all-profiles'),
    path('profile/<int:pk>/', UsersProfileDetailAPIView.as_view(), name='profile-detail')
]
