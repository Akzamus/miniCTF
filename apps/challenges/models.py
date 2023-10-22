from django.db import models
from apps.teams.models import Team


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Challenge(models.Model):
    name = models.CharField(
        max_length=250,
        unique=True,
        null=False,
        blank=False
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE
    )
    description = models.CharField(
        max_length=1000,
        null=False,
        blank=True,
        default=""
    )
    points = models.PositiveIntegerField(
        null=False,
        blank=False
    )
    file = models.FileField(
        null=True,
        blank=True,
        upload_to="challenges/"
    )

    def __str__(self):
        return self.name


class Assignment(models.Model):
    correct_answer = models.CharField(
        max_length=500,
        null=False,
        blank=False
    )
    team = models.ForeignKey(
        to=Team,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    challenge = models.ForeignKey(
        to=Challenge,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.team.name}_{self.challenge.name}"

    class Meta:
        unique_together = ('team', 'challenge')
