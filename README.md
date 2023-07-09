# turbo-lamp
RabbitMQ + Python: Creates task producer that works with several consumers

Producer creates tasks, consumers receives these tasks.
- If consumer1 is busy with a task, consumer2 will take the new tasks and so on.
- If one consumer is busy or occupied with processing a task, the other consumer will be able to pick up and process the next available task from the queue.

### RabbitMQ

Run from docker:

    # version 3.12
    docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management