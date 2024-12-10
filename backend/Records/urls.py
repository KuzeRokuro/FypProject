from django.urls import path
from . import views

urlpatterns = [
    path('api/players/', views.get_players, name='get_players'),  # API endpoint
    path('players/', views.players_page, name='players_page'),    # Webpage view
    path('', views.players_page, name='default'),                 # Default route
]
