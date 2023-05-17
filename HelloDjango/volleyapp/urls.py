from aiohttp.web_routedef import view
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_shema_view
from . import views, routers

shema_view = swagger_get_shema_view(
    openapi.Info(
        title="Posts API",
        default_version='1.0.0',
        description="API documentation of App"
    ),
    public=True,
)

urlpatterns = [
    path('api/v1/',
         include([
             path('swagger/', shema_view.with_ui('swagger', cache_timeout=0)),  # Все апишки
             path('', include(routers.routerUser.urls)),
             path('register/', views.RegistrUserView.as_view(), name='register'),
             path('', include(routers.routerTeams.urls), name='teams'),
             path('', include(routers.routerCoach.urls), name='coach'),
             path('teams/type/', views.TypeTeamAPIViewSet.as_view(), name='type_team'),
             path('', include(routers.routerTournaments.urls), name='tournaments'),
             path('tournaments/<int:tournament_id>/on-teams/', views.TeamsOnTournamentsAPIView.as_view(),
                  name='teams_on_tournament_list'),
             path('teams/<int:team_id>/on-tournaments/', views.TournamentsOnTeamAPIView.as_view(),
                  name='tournaments-on-team_list/'),
             path('teams/<int:team_id>/players/', views.PlayersOnTeamAPIView.as_view(), name='players'),
             path('', include(routers.routerJudge.urls), name='judge')
         ]))
]
