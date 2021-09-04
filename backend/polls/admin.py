from django.contrib import admin
from . import models


class QuestionInline(admin.TabularInline):
    model = models.Question


class PollAdmin(admin.ModelAdmin):
    inlines = (QuestionInline, )


class AnswerInline(admin.TabularInline):
    model = models.Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = (AnswerInline,)
    list_display = ('poll', 'q_type', 'text')


admin.site.register(models.Poll, PollAdmin)
admin.site.register(models.Question, QuestionAdmin)
