"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from Home import views as home_views
from Records import urls
from .views import PlayerView,MatchView,Match,players_by_tournament, PredictView

urlpatterns = [
    *urls.urlpatterns,
    path('', home_views.homepage, name='homepage'),  # Root URL -> Home app
    path('admin/', admin.site.urls),
    path('Records/', include('Records.urls')),  # Other app URLs
    path('Player/', PlayerView.as_view(), name='player_api'),
    path('Match/', MatchView.as_view(), name='match_api'),
    path('Records/PlayersByTournament/<int:tournament_id>/', players_by_tournament, name='players_by_tournament'),
    path('predict/', PredictView.as_view(), name='predict'),
]

