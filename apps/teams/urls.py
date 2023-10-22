from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import LoginForm
from core.settings import LOGIN_URL


from apps.teams.views import get_team_info

app_name = 'teams'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='teams/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(next_page=LOGIN_URL), name="logout"),
    path('<str:team_name>/', get_team_info, name="team")
]
