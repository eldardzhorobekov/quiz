from django.db import models

from .const import Q_TYPES, Q_TEXT


class Poll(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

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
