from rest_framework import routers
from . import views

routerUser = routers.SimpleRouter()
routerUser.register(r'users', views.UserAPIViewSet)

routerCoach = routers.SimpleRouter()
routerCoach.register(r'coach', views.CoachAPIViewSet)

routerTypeTeam = routers.SimpleRouter()
routerTypeTeam.register(r'typeTeam', views.TypeTeamAPIViewSet)

routerTeams = routers.SimpleRouter()
routerTeams.register(r'teams', views.TeamAPIViewSet)

routerTournaments = routers.SimpleRouter()
routerTournaments.register(r'tournaments', views.TournamentAPIViewSet)
