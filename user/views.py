from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import status, viewsets

from .models import User
from .serializer import UserSerializer


# Create your views here.


class UserView(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            instance = request.user
            serializer = UserSerializer(instance)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)