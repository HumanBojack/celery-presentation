import os

from fastapi import FastAPI
from celery import Celery

# Create a Celery instance with Redis broker and backend
celery = Celery(
    "tasks", broker=os.environ.get("REDIS_URI"), backend=os.environ.get("REDIS_URI")
)

# Create a FastAPI instance
app = FastAPI()


# Define the / route, which returns a welcome message
@app.get("/")
def read_root():
    return {"Hello": "World"}


# Define the ADD route, which calls the Celery task in order to add numbers together
@app.post("/add")
def add(x: int, y: int):
    # Call the Celery task and get the task id
    task = celery.send_task("add", args=[x, y])

    return {"task_id": task.id}


# Define the SLEEP route, which calls the Celery task in order to sleep for a given time
@app.post("/sleep")
def sleep(seconds: int):
    # Call the Celery task and get the task id
    task = celery.send_task("sleep", args=[seconds])

    return {"task_id": task.id}


# Define the STATUS route, which returns the status of a previously created task
@app.get("/status/{task_id}")
def get_result(task_id: str):
    # Get the result of the task from the queue
    result = celery.AsyncResult(task_id)
    # Return the task id, status, and result
    return {"task_id": task_id, "status": result.status, "result": result.result}
