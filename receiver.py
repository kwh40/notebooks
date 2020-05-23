import s3i
import time
import requests
import pykka


class Receiver(pykka.ThreadingActor):
    def __init__(self, endpoint, idp, callbackActor, interval=2):
        super().__init__(self)
        self.interval = interval
        self.endpoint = endpoint
        self.idp = idp
        self.callbackActor = callbackActor

    def receive(self):
        access_token = self.idp.get_token(s3i.TokenType.ACCESS_TOKEN)
        headers = {'Content-Type': 'application/pgp-encrypted',
                   'Authorization': 'Bearer ' + access_token}
        response = requests.get(
            url="https://broker.s3i.vswf.dev/"+self.endpoint, headers=headers)
        return(response.text)

    def start_receiving(self):
        # def receive():
        #    access_token = self.idp.get_token(s3i.TokenType.ACCESS_TOKEN)
        #    headers = {'Content-Type': 'application/pgp-encrypted',
        #               'Authorization': 'Bearer ' + access_token}
        #    response = requests.get(
        #        url="https://broker.s3i.vswf.dev/"+self.endpoint, headers=headers)
        #    return(response.text)
        try:
            while True:
                incomingMessage = self.receive()
                if not(len(incomingMessage) == 0):
                    self.callbackActor.callback(incomingMessage)
                    return incomingMessage
                time.sleep(2)
        except KeyboardInterrupt:
            print("[S3I] Stop receiving messages")
