from django.contrib import admin

from .models import Poll, Question, Answer


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class PollAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class PollAdmin(admin.ModelAdmin):
    pass
