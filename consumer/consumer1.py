# Individual Python scripts for each consumer1

import pika
import json


# Define the callback function for processing tasks
def process_task(ch, method, properties, body):
    task = json.loads(body)

    # Process the task here
    print("Consumer 1 received task:", task)

    # Acknowledge the task completion
    ch.basic_ack(delivery_tag=method.delivery_tag)


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
