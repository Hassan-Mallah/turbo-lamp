#  The main Python script for the producer
import pika
import json

# establish a connection to RabbitMQ
host = 'localhost'
connection = pika.BlockingConnection(pika.ConnectionParameters(host))
channel = connection.channel()

# declare the queue, durable to save queue when restart
channel.queue_declare(queue='task_queue', durable=True)

# prepare the task data
task = {
    'id': 1,
    'name': 'Task 1',
    'data': {
        'param1': 'value1',
        'param2': 'value2'
    }
}

# Convert the task data to JSON format
task_json = json.dumps(task)
