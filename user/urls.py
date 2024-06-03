from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import UserView , login , ProfileView

router = DefaultRouter()
router.register(r'users', UserView, basename='user')
router.register(r'profile', ProfileView, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login, name='login'),
]