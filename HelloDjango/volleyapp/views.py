from django.shortcuts import render
from rest_framework import generics, viewsets, status, mixins
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from . import models, serializers
from rest_framework.response import Response


class RegistrUserView(CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserRegistrSerializer
    # Права доступа
    permission_classes = [AllowAny]

    # Метод создания нового пользователя
    def post(self, request, *args, **kwargs):
        serializer = serializers.UserRegistrSerializer(data=request.data)
        data = {}

        # Проверка данных на валидность
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class UserAPIViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()


class CoachAPIViewSet(mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = serializers.CoachSerializer
    queryset = models.Coach.objects.all()


class CoachAPIViewSet(mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = serializers.CoachSerializer
    queryset = models.Coach.objects.all()


class TypeTeamAPIViewSet(mixins.RetrieveModelMixin,
                         mixins.ListModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = serializers.TypeTeamSerializer
    queryset = models.TypeTeam.objects.all()


class TeamAPIViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamsSerializer


class TournamentAPIViewSet(viewsets.ModelViewSet):
    queryset = models.Tournament.objects.all()
    serializer_class = serializers.TournamentsSerializer
