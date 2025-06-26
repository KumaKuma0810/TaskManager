from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from .models import *


class TaskSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
        # validated_date - это словарь с данными, которые были переданы через сериализатор
        # сначала "парсит" данные из запроса, затем вызывает метод .is_valid()
        # Если все проверки прошли успешно, сериализатор сохраняет очищенные и проверенные
        # данные в атрибуте validated_data.
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
