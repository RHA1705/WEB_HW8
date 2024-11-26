import pika
from models import Contact
from faker import Faker
from datetime import datetime

def produce_contacts(connection, count=10):
    channel = connection.channel()
    channel.queue_declare(queue='email_queue', durable=True)

    fake = Faker()
    for _ in range(count):
        contact = Contact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email()
        )
        contact.save()
        channel.basic_publish(exchange='',
                              routing_key='email_queue',
                              body=str(contact.id),
                              properties=pika.BasicProperties(
                                  delivery_mode=2
  # persistent message
                              ))
        print(f"Sent contact ID {contact.id} to queue")

if __name__ == '__main__':
    # Parametry połączenia z RabbitMQ (zastąp placeholderami)
    credentials = pika.PlainCredentials('your_user', 'your_password')
    parameters = pika.ConnectionParameters('your_rabbitmq_host', 5672, '/', credentials)

    # Utworzenie połączenia
    connection = pika.BlockingConnection(parameters)
    try:
        produce_contacts(connection, count=100)  # Wygeneruj 100 kontaktów
    finally:
        connection.close()

