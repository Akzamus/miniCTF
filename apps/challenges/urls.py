from django.urls import path
from .views import index, submit_challenge, scoreboard
from django.conf import settings
from django.conf.urls.static import static

app_name = 'challenges'

urlpatterns = [
    path('', index, name='index'),
    path('submit/', submit_challenge, name="submit_challenge"),
    path('scoreboard/', scoreboard, name="scoreboard")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
