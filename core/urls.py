from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='challenges/', permanent=True)),
    path('challenges/', include('apps.challenges.urls')),
    path('teams/', include('apps.teams.urls')),
    path('admin/', admin.site.urls),
]
