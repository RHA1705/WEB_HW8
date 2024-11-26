import pika
from models import Contact
from datetime import datetime

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

        # Tutaj umieść rzeczywistą logikę wysyłania email, np. używając biblioteki smtplib
        # send_email(contact.email, subject, message)

    except Contact.DoesNotExist:
        print(f"Contact with ID {contact_id} not found")

if __name__ == '__main__':
    # Parametry połączenia z RabbitMQ (zastąp placeholderami)
    credentials = pika.PlainCredentials('your_user', 'your_password')
    parameters = pika.ConnectionParameters('your_rabbitmq_host', 5672, '/', credentials)

    # Utworzenie połączenia
    connection = pika.BlockingConnection(parameters)

    # Deklaracja kolejki
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')

    # Konsumowanie wiadomości
    channel.basic_consume(queue='email_queue', on_message_callback=consume_messages, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()