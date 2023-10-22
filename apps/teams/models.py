from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Team(models.Model):
    name = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is None:
            User.objects.create_user(
                username=self.name,
                email=self.email,
                password=self.password
            )
        else:
            user = User.objects.get(pk=self.pk)
            user.username = self.name
            user.email = self.email
            user.set_password(self.password)
            user.save()

        super().save(*args, **kwargs)


@receiver(pre_delete, sender=Team)
def team_pre_delete(sender, instance, **kwargs):
    user = User.objects.get(email=instance.email)
    if user:
        user.delete()
