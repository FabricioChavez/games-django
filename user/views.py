from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import User
from .serializers import UserSerializer
import logging
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        headers = self.get_success_headers(serializer.data)
        logger.info(f'User created: {user.username}, Token: {token.key}')
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
@authentication_classes([])
def login(request, format=None):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)


class ProfileView(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        logger.info(f'Authorization header: {request.headers.get("Authorization")}')
        user = request.user
        logger.info(f'Authenticated user: {user}')
        serializer = UserSerializer(user)
        return Response(serializer.data)