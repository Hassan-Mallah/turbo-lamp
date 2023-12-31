# Individual Python scripts for each consumer2

import pika
import json
from time import sleep


# Define the callback function for processing tasks
def process_task(ch, method, properties, body):
    task = json.loads(body)

    # Process the task here
    print("Consumer 2 received task:", task['name'])
    sleep(5)

    # Acknowledge the task completion
    ch.basic_ack(delivery_tag=method.delivery_tag)

    print("Consumer 2 finished task:", task['name'])


# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='task_queue', durable=True)

# Specify the number of tasks this consumer can handle at a time
channel.basic_qos(prefetch_count=1)

# Start consuming tasks from the queue
channel.basic_consume(queue='task_queue', on_message_callback=process_task)

# Begin consuming tasks
channel.start_consuming()
