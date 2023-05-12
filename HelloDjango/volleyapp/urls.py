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
             path('registr/', views.RegistrUserView.as_view(), name='registr'),
             path('', include(routers.routerTeams.urls), name='teams'),
             path('', include(routers.routerCoach.urls), name='coach'),
             path('', include(routers.routerTypeTeam.urls), name='type_team'),
             path('', include(routers.routerTournaments.urls), name='tournaments'),
         ]))
]
