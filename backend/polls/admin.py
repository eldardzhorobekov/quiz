from django.contrib import admin
from . import models
from .forms import PollForm


class QuestionInline(admin.TabularInline):
    model = models.Question
    extra = 0


class PollAdmin(admin.ModelAdmin):
    form = PollForm
    inlines = (QuestionInline, )


class AnswerInline(admin.TabularInline):
    model = models.Answer
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = (AnswerInline,)
    list_display = ('poll', 'q_type', 'text')


admin.site.register(models.Poll, PollAdmin)
admin.site.register(models.Question, QuestionAdmin)
