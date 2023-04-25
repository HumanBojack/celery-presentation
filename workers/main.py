import os
import time

from celery import Celery

# Create a Celery instance with a Redis broker and backend
celery = Celery(
    "tasks", broker=os.environ.get("REDIS_URI"), backend=os.environ.get("REDIS_URI")
)


# Define a Celery task that adds two numbers
@celery.task(name="add")
def add(x, y):
    return x + y


# Define a Celery task that takes a given time to complete
@celery.task(name="sleep")
def sleep(seconds):
    time.sleep(seconds)
    return f"Done sleeping for {seconds} seconds"
