from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Player', views.PlayerViewSet)
router.register(r'Tournament', views.TournamentViewSet)
router.register(r'Match', views.MatchViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
