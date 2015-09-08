#from scrapy.utils.serialize import ScrapyJSONEncoder
#from pika import BlockingConnection, ConnectionParameters

#from src import settings
from requests import post
import json

class scraperPipeline(object):

    def process_item (self, item, spider):
        with open("%s.txt" % str(item['file_']), "a") as a:
            a.write(str(item['reviews']))
        return item

        """
        payload = {'reviews': item['reviews']}
        print payload
        r = post("http://localhost:5000/reviews", headers={'Content-Type':'application/json'}, data=json.dumps(payload))
        print r
        return item

    @classmethod
    def from_settings(cls, settings):
        host_name = settings.get('FLASK_HOST')
        port = settings.get('FLASK_PORT')
        return cls(host_name, port)
    
    #Emit processed items to a RabbitMQ exchange/queue
    def __init__(self, host_name, port, userid, password, virtual_host, encoder_class):
        self.connection = BlockingConnection(ConnectionParameters(
                                                            host='localhost'))
        self.channel = self.connection.channel()
        self.encoder = encoder_class()
        self.channel.exchange_declare(exchange='rev', type='direct')

    @classmethod
    def from_settings(cls, settings):
        host_name = settings.get('BROKER_HOST')
        port = settings.get('BROKER_PORT')
        userid = settings.get('BROKER_USERID')
        password = settings.get('BROKER_PASSWORD')
        virtual_host = settings.get('BROKER_VIRTUAL_HOST')
        encoder_class = settings.get('MESSAGE_Q_SERIALIZER', ScrapyJSONEncoder)
        return cls(host_name, port, userid, password, virtual_host, encoder_class)

    def process_item(self, item, spider):
        self.channel.basic_publish(exchange='rev',
                                    routing_key=str(12345),
                                    body=self.encoder.encode(dict(item)))
    """
