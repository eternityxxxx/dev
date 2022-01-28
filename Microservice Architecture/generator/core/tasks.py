from celery_app import app

from .models import Event


@app.task(name=create_event)
def create_event(number):
    Event.objects.create(number=number)
