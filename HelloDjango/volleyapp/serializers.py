import codecs

from rest_framework import serializers
from . import models
from django.forms import model_to_dict
from .models import Role


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
    role = serializers.CharField(source='role.role', read_only=True)

    class Meta:
        model = models.User
        fields = ('id', 'username', 'surname', 'middle_name', 'age', 'role')


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coach
        fields = '__all__'

    def to_representation(self, instance):
        new_data = {
            'id': instance.id,
            'user': {
                'user_id': instance.user.id,
                'name': instance.user.username,
                'surname': instance.user.surname,
                'middle_name': instance.user.middle_name,
            },
            'category': instance.category
        }
        return new_data


class TypeTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TypeTeam
        fields = '__all__'


class TeamsSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    logo = serializers.SerializerMethodField()
    type = TypeTeamSerializer()
    coach = CoachSerializer()

    class Meta:
        model = models.Team
        fields = '__all__'

    def get_photo(self, obj):
        return obj.photo.url if obj.photo else None

    def get_logo(self, obj):
        return obj.logo.url if obj.logo else None

    def to_representation(self, instance):
        new_data = {
            'id': instance.id,
            'name': instance.name,
            'photo': {
                'photo': self.get_photo(instance),
                'logo': self.get_logo(instance),
            },
            'foundation_date': instance.foundation_date,
            'sponsor': {
                'sponsor': instance.sponsor,
                'sponsor_logo': instance.sponsor_logo,
            },
            'type': self.fields['type'].to_representation(instance.type),
            'coach': {
                'user_id': instance.coach.user.id,
                'name': instance.coach.user.username,
                'surname': instance.coach.user.surname,
                'middle_name': instance.coach.user.middle_name
            }
        }

        return new_data


class TournamentsSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = models.Tournament
        fields = '__all__'

    def get_photo(self, obj):
        return obj.photo.url if obj.photo else None

    def to_representation(self, instance):
        new_data = {
            'id': instance.id,
            'name': instance.name,
            'date': {
                'start_date': instance.start_date,
                'date_end': instance.date_end
            },
            'description': instance.description,
            'photo': self.get_photo(instance)
        }
        return new_data


class TeamsOnTournamentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TeamOnTournament
        fields = ['id', 'team', 'tournament', 'league', 'subgroup', 'place']

    def to_representation(self, instance):
        new_data = {
            'id': instance.id,
            'team': {
                'id_team': instance.team.id,
                'name_team': instance.team.name
            },
            'tournament': {
                'id_tournament': instance.tournament.id,
                'name_tournament': instance.tournament.name
            },
            'league': instance.league.league if instance.league else None,
            'subgroup': instance.subgroup.subgroup if instance.subgroup else None,
            'place': instance.place
        }
        return new_data


class PlayersOnTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Player
        fields = '__all__'

    def to_representation(self, instance):
        new_data = {
            'id': instance.id,
            'is_captain': instance.is_captain,
            'amplua': instance.amplua.amplua,
            'team': instance.team.name,
            'user': {
                'id_user': instance.user.id,
                'name': instance.user.username,
                'surname': instance.user.surname,
            },
            'game_number': instance.game_number
        }
        return new_data


class PlayersSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Player
        fields = '__all__'


class JudgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Judge
        fields = '__all__'

    def to_representation(self, instance):
        new_data = {
            'id': instance.id,
            'category': instance.category,
            'user': {
                'user_id': instance.user.id,
                'name': instance.user.username,
                'surname': instance.user.surname
            }
        }
        return new_data


