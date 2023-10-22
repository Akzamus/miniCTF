from django.contrib import admin
from .models import Assignment, Challenge, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'points')
    list_filter = ('category',)
    ordering = ('category__name', 'points')


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'completed_at')
    list_filter = ('team', 'challenge')
    ordering = ('team__name', 'challenge__name', 'completed_at')
