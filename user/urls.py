from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

urlpatterns = [
    path('', views.UserView.as_view(), name='user'),
    path('', include(router.urls)),
]