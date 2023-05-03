from __future__ import unicode_literals,absolute_import
# from celery import shared_task
from .models import Product
from celery import Celery,shared_task
from django.forms.models import model_to_dict
import json
app=Celery()
@app.task
def update(id,title,image,likes):
    p = Product.objects.get(id=id)
    p.title = title
    p.image=image
    p.likes=likes
    p.save()
    data=json.dumps(model_to_dict(p))
    return data

@shared_task
def add(x,y):
    print('hello')
    return x+y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def update(id,title,image,likes):
    p = Product.objects.get(id=id)
    p.title = title
    p.image=image
    p.likes=likes
    p.save()
    data=json.dumps(model_to_dict(p))

    return data