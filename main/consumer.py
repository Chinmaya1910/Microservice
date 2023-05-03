import pika
import json
from flask import current_app
from main import Product, db, app
params = pika.URLParameters('amqps://fiauhljg:qJT9wy3FSfKSu-GhCGhf6emkzAln93ug@puffin.rmq2.cloudamqp.com/fiauhljg')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch,method,properties,body):
    print('Recieved in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        with app.app_context():
            product = Product(id=data['id'], title=data['title'], image=data['image'],likes=data['likes'])
            db.session.add(product)
            db.session.commit()
        print('Product Created')

    elif properties.content_type == 'product_updated':
        with app.app_context():
            product = db.session.get(Product,data['id'])
            product.title = data['title']
            product.image = data['image']
            db.session.commit()
        print('Product Updated')

    elif properties.content_type == 'product_deleted':
        with app.app_context():
            product = db.session.get(Product,data)
            db.session.delete(product)
            db.session.commit()
        print('Product Deleted')

channel.basic_consume(queue='main',on_message_callback=callback,auto_ack=True)

print('Started Consuming')

channel.start_consuming()
# connection.close()
channel.close()