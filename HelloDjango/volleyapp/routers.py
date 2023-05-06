from rest_framework import routers
from . import views

routerUser = routers.SimpleRouter()
routerUser.register(r'users', views.UserAPIViewSet)