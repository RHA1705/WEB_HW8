import pika
from models import Contact
from faker import Faker
import connect

def generate_fake_contacts(count):
    fake = Faker()
    for _ in range(count):
        contact = Contact(fullname=fake.name(), email=fake.email())
        contact.save()
        # Відправка повідомлення в RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='email_queue')

        channel.basic_publish(exchange='', body=str(contact.id),
 routing_key='email_queue')
        connection.close()

if __name__ == '__main__':
    generate_fake_contacts(10)  # Згенерувати 100 фейкових контактів
# def produce_contacts(connection, count=10):
#     channel = connection.channel()
#     channel.queue_declare(queue='email_queue')
#
#     fake = Faker()
#     for _ in range(count):
#         contact = Contact(
#             fullname = fake.name(),
#             email=fake.email()
#
#         )
#         contact.save()
#         channel.basic_publish(exchange='',
#                               routing_key='email_queue',
#                               body=str(contact.id),
#                               properties=pika.BasicProperties(
#                                   delivery_mode=2
#   # persistent message
#                               ))
#         print(f"Sent contact ID {contact.id} to queue")
#
# if __name__ == '__main__':
#     # Parametry połączenia z RabbitMQ (zastąp placeholderami)
#     credentials = pika.PlainCredentials('guest', 'guest')
#     parameters = pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)
#
#     # Utworzenie połączenia
#     connection = pika.BlockingConnection(parameters)
#     try:
#         produce_contacts(connection, count=10)  # Wygeneruj 10 kontaktów
#     finally:
#         connection.close()

