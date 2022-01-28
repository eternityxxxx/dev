from django.db import models


class Event(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    number = models.CharField(max_length=255)
