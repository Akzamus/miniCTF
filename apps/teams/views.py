from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect


from .models import Team
from apps.challenges.models import Assignment


@login_required
def get_team_info(request, team_name):
    if request.method == 'GET':
        user = request.user

        if user.is_superuser and team_name == "me":
            return redirect('challenges:scoreboard')

        if team_name == "me":
            team = get_object_or_404(Team, name=user.username)
        else:
            team = get_object_or_404(Team, name=team_name)

        completed_assignments = Assignment.objects.filter(team=team, completed_at__isnull=False)

        total_score = completed_assignments.aggregate(total_score=Sum('challenge__points')).get('total_score', 0)
        solved_challenges = [assignment.challenge for assignment in completed_assignments]

        if total_score is None:
            total_score = 0

        data = {
            'team': team,
            'solved_challenges': solved_challenges,
            'total_score': total_score
        }

        return render(request, 'teams/team.html', data)
