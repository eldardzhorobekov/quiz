from django.contrib import admin
from . import models


class QuestionInline(admin.TabularInline):
    model = models.Question
    extra = 0


class PollAdmin(admin.ModelAdmin):
    inlines = (QuestionInline, )

    def get_readonly_fields(self, request, obj=None):
        return ['date_start'] if obj else []


class AnswerInline(admin.TabularInline):
    model = models.Answer
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = (AnswerInline,)
    list_display = ('poll', 'q_type', 'text')


admin.site.register(models.Poll, PollAdmin)
admin.site.register(models.Question, QuestionAdmin)
