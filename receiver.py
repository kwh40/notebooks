import pykka
#from s3i import 
import pika
import time
from s3i import Broker, TokenType
import logging
logging.basicConfig(level=logging.ERROR)
logging.getLogger('pykka').setLevel(logging.ERROR)

def callback(ch, method, properties, body):
    body_str = body.decode('utf8').replace("'", '"')  # convert bytes to str
    print("[S3I][" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "]: A new message has been received", body_str)
    with open("C:/Users/Marlene/Documents/MMI-Arbeit/Workshop/file.txt", 'a') as out_file:
        out_file.write("Hello")

class Receiver(pykka.ThreadingActor):
    def __init__(self, idp, thingId):
        super().__init__()
        self.idp = idp
        self.thingId = thingId
        self.receive()

    def receive(self):
        access_token = self.idp.get_token(TokenType.ACCESS_TOKEN)
        broker = Broker(auth_form='Username/Password', username=" ", password=access_token, host="rabbitmq.s3i.vswf.dev")
        endpoint = "s3ibs://"+self.thingId
        broker.receive(endpoint, callback)
        #broker.receive(endpoint, lambda : print("Hello"))


                                