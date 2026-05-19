import json
from kafka import KafkaProducer
from core import settings

# producer
brokers = "rocket-03.srvs.cloudkafka.com:9094,rocket-01.srvs.cloudkafka.com:9094,rocket-02.srvs.cloudkafka.com:9094"

topic = '0iuij7z1-faer'

producer = None

if settings.DEBUG:
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x: json.dumps(x, default=str).encode('utf-8')
                             )
else:
    producer = KafkaProducer(bootstrap_servers=brokers,
                             security_protocol='SASL_SSL',
                             sasl_mechanism='SCRAM-SHA-256',
                             sasl_plain_username='0iuij7z1',
                             sasl_plain_password='G7WL8CTe6_xYF-yziEHXjDaOLbsXJRHy',
                             value_serializer=lambda x: json.dumps(x, default=str).encode('utf-8')
                             )


def on_send_success(record_metadata):
    print(record_metadata.topic)
    # print(record_metadata.partition)
    # print(record_metadata.offset)


def on_send_error(excp):
    print('I am an errback')
    # handle exception


def publish(method: str, body: dict):
    producer.send(topic, key=method.encode('UTF-8'), value=body).add_callback(
        on_send_success).add_errback(on_send_error)
    print(f'Topic :{topic}  Key :{method}   published.')

    # block until all async messages are sent
    producer.flush()
