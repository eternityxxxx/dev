from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class Answer(models.Model):
    title = models.CharField(max_length=128, verbose_name='Answer title')
    is_correct = models.BooleanField(default=False, verbose_name='Correctness')
    number_of_choice = models.IntegerField(default=0, verbose_name='The number of answer choice')

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=128, verbose_name='Question title')
    response_time = models.TimeField(null=True, verbose_name='Question response time')
    score = models.PositiveSmallIntegerField(default=0, validators=(MinValueValidator(0), MaxValueValidator(10)),
                                             verbose_name='Answer score')

    answer = models.ForeignKey(Answer, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.title) + ' | ' + str(self.score)


class Poll(models.Model):
    title = models.CharField(max_length=128, verbose_name='Poll title')
    description = models.CharField(max_length=255, verbose_name='Poll description')
    created_at = models.DateTimeField(auto_now_add=True)
    ready_at = models.DateTimeField(verbose_name='Poll ready date', default=now)
    response_time = models.TimeField(null=True)

    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
