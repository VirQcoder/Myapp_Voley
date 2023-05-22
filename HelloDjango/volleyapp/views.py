from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, viewsets, status, mixins
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from . import models, serializers
from rest_framework.response import Response


class BaseModelAPIViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {'data': response.data}
        return response


class BaseGenericAPIViewSet(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {'data': response.data}
        return response


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

    def list(self, request, *args, **kwargs):
        res = super(UserAPIViewSet, self).list(request, *args, **kwargs)
        res.data = {'data': res.data}
        return res


class CoachAPIViewSet(mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = serializers.CoachSerializer
    queryset = models.Coach.objects.all()

    def list(self, request, *args, **kwargs):
        res = super(CoachAPIViewSet, self).list(request, *args, **kwargs)
        res.data = {'data': res.data}
        return res


class TypeTeamAPIViewSet(BaseGenericAPIViewSet):
    serializer_class = serializers.TypeTeamSerializer
    queryset = models.TypeTeam.objects.all()


class TeamAPIViewSet(BaseModelAPIViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamsSerializer


class TournamentAPIViewSet(BaseModelAPIViewSet):
    queryset = models.Tournament.objects.all()
    serializer_class = serializers.TournamentsSerializer


class TeamsOnTournamentsAPIView(BaseGenericAPIViewSet):
    serializer_class = serializers.TeamsOnTournamentsSerializer

    def get_queryset(self):
        tournament_id = self.kwargs['tournament_id']
        queryset = models.TeamOnTournament.objects.filter(tournament_id=tournament_id)
        return queryset


class TournamentsOnTeamAPIView(BaseGenericAPIViewSet):
    serializer_class = serializers.TeamsOnTournamentsSerializer

    def get_queryset(self):
        team_id = self.kwargs['team_id']
        queryset = models.TeamOnTournament.objects.filter(team_id=team_id)
        return queryset


class PlayersOnTeamAPIView(BaseGenericAPIViewSet):
    serializer_class = serializers.PlayersOnTeamSerializer

    def get_queryset(self):
        team_id = self.kwargs['team_id']  # Получение идентификатора команды из URL
        queryset = models.Player.objects.filter(team_id=team_id)
        return queryset


class JudgeAPIView(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = models.Judge.objects.all()
    serializer_class = serializers.JudgeSerializer

    def list(self, request, *args, **kwargs):
        res = super(JudgeAPIView, self).list(request, *args, **kwargs)
        res.data = {'data': res.data}
        return res
