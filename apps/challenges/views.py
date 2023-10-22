from django.contrib.auth.decorators import login_required
from django.db.models import IntegerField, F, Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils import timezone

from apps.teams.models import Team
from .models import Assignment, Category, Challenge


@login_required
def index(request):
    if request.method == 'GET':
        user = request.user
        categories = []

        if not user.is_superuser:
            team = get_object_or_404(Team, name=user.username)

            solved_challenge_ids = Assignment.objects \
                .filter(team=team) \
                .exclude(completed_at=None) \
                .values_list('challenge', flat=True)
        else:
            solved_challenge_ids = []

        for category in Category.objects.all():
            categories.append(
                {
                    'name': category.name,
                    'challenges': category.challenge_set.all().order_by("points")
                }
            )

        return render(
            request,
            'challenges/challenges.html',
            {
                'categories': categories,
                'solved_challenge_ids': solved_challenge_ids
            }
        )


@login_required
def submit_challenge(request):
    if request.method == 'POST' and not request.user.is_superuser:
        challenge = get_object_or_404(Challenge, pk=int(request.POST['challenge_pk']))
        team = get_object_or_404(Team, name=request.user.username)
        assignment = get_object_or_404(Assignment, team=team, challenge=challenge)

        if assignment.completed_at:
            return JsonResponse({'result': 'ALREADY'})

        if assignment.correct_answer == request.POST['answer']:
            assignment.completed_at = timezone.now()
            assignment.save()
            return JsonResponse({'result': 'CORRECT'})

        return JsonResponse({'result': 'INCORRECT'})


@login_required
def scoreboard(request):
    teams = Team.objects.annotate(
        total_score=Sum(
            F('assignment__challenge__points'),
            output_field=IntegerField()
        )
    )
    return render(request, 'challenges/scoreboard.html', {'teams': teams})
