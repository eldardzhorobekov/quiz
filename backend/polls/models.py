from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import ValidationError

from .const import Q_TYPES, Q_TEXT


class Poll(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    def clean(self):
        if self.date_start >= self.date_end:
            raise ValidationError('date_end', 'Poll end date must be after start date')

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField()
    q_type = models.IntegerField(choices=Q_TYPES, default=Q_TEXT)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')


class Attempt(models.Model):
    user = models.ManyToManyField(get_user_model(), related_name='attempts')
    poll = models.ForeignKey(Poll, on_delete=models.SET_NULL, related_name='attempts', null=True)
    # answers = models.JsonField()