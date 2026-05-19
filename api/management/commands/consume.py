import json
from kafka import KafkaConsumer
from core import settings
from django.core.management.base import BaseCommand
from api.tasks import create_room, create_vehicle, create_reservation


class Command(BaseCommand):
    help = 'Start Consumer'

    def handle(self, *args, **options):
        brokers = "rocket-03.srvs.cloudkafka.com:9094,rocket-01.srvs.cloudkafka.com:9094,rocket-02.srvs.cloudkafka.com:9094"
        topic = '0iuij7z1-faer'
        consumer = None
        if settings.DEBUG:
            consumer = KafkaConsumer(topic,
                                     bootstrap_servers=['localhost:9092'],
                                     value_deserializer=lambda x: json.loads(x.decode('utf-8'))
                                     )
        else:
            consumer = KafkaConsumer(topic,
                                     bootstrap_servers=brokers,
                                     security_protocol='SASL_SSL',
                                     sasl_mechanism='SCRAM-SHA-256',
                                     sasl_plain_username='0iuij7z1',
                                     sasl_plain_password='G7WL8CTe6_xYF-yziEHXjDaOLbsXJRHy',
                                     auto_offset_reset='latest',
                                     value_deserializer=lambda x: json.loads(x.decode('utf-8'))
                                     )

        print('Start consuming')
        for message in consumer:
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                 message.offset, message.key, message.value))

            if message.key == b'create_room':
                create_room(message.value)

            if message.key == b'create_vehicle':
                create_vehicle(message.value)

            if message.key == b'create_reservation':
                create_reservation(message.value)
