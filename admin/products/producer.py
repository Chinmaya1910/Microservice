import pika
import json
params = pika.URLParameters('amqps://fiauhljg:qJT9wy3FSfKSu-GhCGhf6emkzAln93ug@puffin.rmq2.cloudamqp.com/fiauhljg')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties= pika.BasicProperties(method)
    channel.basic_publish(exchange='',routing_key='main',body=json.dumps(body),properties=properties)