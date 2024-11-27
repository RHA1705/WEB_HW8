import pika
from models import Contact
from datetime import datetime
import connect

def consume_messages(ch, method, properties, body):
    """
    Konsumuje wiadomości z kolejki RabbitMQ, aktualizuje status kontaktu w bazie danych i symuluje wysłanie email.

    Args:
        ch: Kanał RabbitMQ.
        method: Metoda dostarczenia wiadomości.
        properties: Właściwości wiadomości.
        body: Treść wiadomości (ID kontaktu).
    """

    contact_id = body.decode()
    try:
        contact = Contact.objects(id=contact_id).get()
        contact.is_sent = True
        contact.updated_at = datetime.utcnow()
        contact.save()
        print(f"Email sent to {contact.email}")

    except Contact.DoesNotExist:
        print(f"Contact with ID {contact_id} not found")

if __name__ == '__main__':

    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)

    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()
    channel.queue_declare(queue='email_queue')

    channel.basic_consume(queue='email_queue', on_message_callback=consume_messages, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()