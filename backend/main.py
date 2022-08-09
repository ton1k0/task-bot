from typing import Optional
from fastapi import FastAPI
from redis_om import HashModel
from database import redis_db
import datetime


app = FastAPI()



class Task(HashModel):
    name: str
    complete: int
    date: Optional[datetime.date] = datetime.date.today()

    class Meta:
        database = redis_db

@app.get('/tasks')
async def all():
    return [format(pk) for pk in Task.all_pks()]

def format(pk:str):
    task = Task.get(pk)

    return {
        'id': task.pk,
        'name': task.name,
        'complete': task.complete,
        'date': task.date
    }

@app.post('/task')
async def create(task: Task):
    return task.save()

@app.put('/task/{pk}')
async def update(pk:str):
    task = Task.get(pk)
    task.complete = 1
    return task.save()


@app.delete('/task/{pk}')
async def delete(pk: str):
    task = Task.get(pk)
    return task.delete(pk)
