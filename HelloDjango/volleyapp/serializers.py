from rest_framework import serializers
from . import models
from django.forms import model_to_dict


class UserRegistrSerializer(serializers.ModelSerializer):
    # Поле для повторения пароля
    password2 = serializers.CharField()

    class Meta:
        model = models.User
        fields = ['username', 'surname', 'age', 'email', 'password', 'password2', 'role', 'is_extra', 'is_staff']

    # Метод для сохранения нового пользователя
    def save(self, *args, **kwargs):
        user = models.User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            surname=self.validated_data['surname'],
            age=self.validated_data['age'],
            role=self.validated_data['role'],
            is_extra=self.validated_data['is_extra'],
            is_staff=self.validated_data['is_staff'],
        )
        # Проверка на валидность пароля
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        # Провекрка на совпадение паролей
        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})

        user.set_password(password)
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'surname', 'role')


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = '__all__'
