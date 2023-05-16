from rest_framework import routers
from . import views

routerUser = routers.SimpleRouter()
routerUser.register(r'users', views.UserAPIViewSet)

routerCoach = routers.SimpleRouter()
routerCoach.register(r'coach', views.CoachAPIViewSet)

routerTeams = routers.SimpleRouter()
routerTeams.register(r'teams', views.TeamAPIViewSet, basename='team')

routerTournaments = routers.SimpleRouter()
routerTournaments.register(r'tournaments', views.TournamentAPIViewSet)

routerJudge = routers.SimpleRouter()
routerJudge.register(r'judge', views.JudgeAPIView)
