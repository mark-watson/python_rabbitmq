import time
from rabbitmq_client import RMQConsumer, ConsumeParams, QueueParams


def on_message(msg, ack=None):
    print("on_message: ", msg)

consumer = RMQConsumer()
consumer.start()
consumer.consume(ConsumeParams(on_message),
                 queue_params=QueueParams("send.py"))

time.sleep(30)
print("done...")


