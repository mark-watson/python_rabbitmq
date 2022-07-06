import time
from rabbitmq_client import RMQProducer, ExchangeParams


def on_confirm(confirmation):
    print("on_confirm:", confirmation)

producer = RMQProducer()
producer.start()
producer.activate_confirm_mode(on_confirm)  # Or don't, depends on your needs

producer.publish(b"body", 
                 exchange_params=ExchangeParams("test-ex3"),
                 routing_key="xx")

time.sleep(30)
print("done...")

