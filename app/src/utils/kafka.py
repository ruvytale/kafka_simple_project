from kafka.producer import KafkaProducer
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


def make_producer():
    producer = KafkaProducer(bootstrap_servers=os.environ["BOOTSTRAP-SERVERS"])
    return producer
