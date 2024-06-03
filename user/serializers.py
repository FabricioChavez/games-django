from rest_framework import serializers
from .models import User

from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'description', 'email', 'phone', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
