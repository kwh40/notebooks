from s3i import IdentityProvider,TokenType, UserMessage, Broker, Directory, Key
from receiver import Receiver
import time 
import base64

{
  "identifier": "s3i:bf5a3b54-1ecc-4195-bc55-cb4757b895d0",
  "secret": "c4d762cd-4ef6-4d99-83c4-b287b832a455"
}

CLIENT = "s3i:4f076127-d9e2-477d-8d42-4453225bfaaa"
SECRET = "5ad8387a-5183-471b-8dfe-da2c7c62557f"

USER = "gebhard"
PASSWORD = "iuzkjh"



#def callback(ch, method, properties, body):
#        body_str = body.decode('utf8').replace("'", '"')  # convert bytes to str
#        print("[S3I][" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "]: A new message has been received", body_str)

def callback(ch, method, properties, body):
    #body_str = body.decode('utf8').replace("'", '"')  # convert bytes to str
    #print("[S3I][" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "]: A new message has been received", body_str)
    
    print("[S3I][" + time.strftime("%Y-%m-%d %H:%M:%S",
                                   time.localtime()) + "]: A new message has been received")
    body_str = body.decode('utf8').replace("'", '"')  # convert bytes to str
    uMsg = UserMessage(msg_blob=body_str)

    """Decrypt the message and verify the signature
    """
    if uMsg.pgpMsg.is_encrypted:
        sec_key = Key(path_demo_dir="key", filename="test_sec.asc")
        #uMsg.decryptAndVerify(pgpKey_sec, os.path.join(
        #        fp, "gpg"), s3i_directory)
        uMsg.decrypt(sec_key.key)
        uMsg.convertPgpToMsg()

    print("[S3I]: Subject of the message: " + uMsg.msg["subject"])
    print("[S3I]: Text of the message:  " + uMsg.msg["text"])

    #attachments_list = list()
    attachments_list = uMsg.msg["attachments"]

    """
    store the attachment file in specified path
    """
    for i in range(len(attachments_list)):
        file = open("received_data", 'wb')
        decode = base64.b64decode(attachments_list[i]["data"])
        file.write(decode)
        print("[S3I]: Attachment " + uMsg.msg["attachments"]
              [i]["filename"] + " of the message is stored in received_data")
        file.close()

username= "KWH-Team"
password= "V4yuJ31izh0GCH36954O"
s3i_identity_provider = IdentityProvider(grant_type='password', identity_provider_url="https://idp.s3i.vswf.dev/", realm='KWH',
                                             client_id="s3i:0c253262-428e-44be-a11a-b83566bd1f68", client_secret="8d9ad853-2bfb-44f1-ad47-bc2a6bad8a03", username=username, password=password)
access_token = s3i_identity_provider.get_token(TokenType.ACCESS_TOKEN)
#access_token = idp.get_token(TokenType.ACCESS_TOKEN)
broker = Broker(auth_form='Username/Password', username=" ", password=access_token, host="rabbitmq.s3i.vswf.dev")
broker.receive("s3ibs://"+"s3i:bf5a3b54-1ecc-4195-bc55-cb4757b895d0", callback)

#idp = IdentityProvider(grant_type='password', identity_provider_url="https://idp.s3i.vswf.dev/", realm='KWH',
#                                             client_id=CLIENT, client_secret=SECRET, username=USER, password=PASSWORD)
#access_token = idp.get_token(TokenType.ACCESS_TOKEN)
#dir = Directory(s3i_dir_url="https://dir.s3i.vswf.dev/api/2/", token=access_token)
#receivers = ["s3i:bf5a3b54-1ecc-4195-bc55-cb4757b895d0"]
#defaultHMIs = [dir.queryThingIDBased(receiver+"/attributes/defaultHMI") for receiver in receivers]#

#broker = Broker(auth_form='Username/Password', username=" ", password=access_token, host="rabbitmq.s3i.vswf.dev")
#receivers_endpoints = ["s3ibs://s3i:bf5a3b54-1ecc-4195-bc55-cb4757b895d0"]
#msg = UserMessage(sender=CLIENT, identifier="test",receivers=receivers_endpoints, subject="Test", text="TestText")
##broker.send(receivers_endpoints,msg.msg.__str__())
##endpoint = "s3ibs://"+CLIENT
##broker.receive(endpoint, callback)

#receiver_proxy = Receiver.start(idp, CLIENT).proxy()
##receiver_proxy.receive()

#print("test")

import uuid
subject = "This is a test" #input('[S3I]: please enter the subject: \n')
text = "This is a text test" #input('[S3I]: please enter the text: \n')
msg_uuid = "s3i:" + str(uuid.uuid4())
replyToEndpoint=None
attachments=None
receivers = ["s3i:bf5a3b54-1ecc-4195-bc55-cb4757b895d0"]
message = UserMessage(sender=CLIENT, identifier=msg_uuid,receivers=receivers, subject=subject, text=text,
                  replyToEndpoint=replyToEndpoint, attachments=attachments)
pgpKey_sec = Key(path_demo_dir="key", filename="test_sec.asc")
message.sign(pgpKey_sec.key)


dir = Directory(s3i_dir_url="https://dir.s3i.vswf.dev/api/2/", token=access_token)
publicKeys_str = dir.getPublicKey(receivers)
#pubKey = Key(key_str = publicKeys)
#message.encrypt(publicKeys)
#print(message.pgpMsg.__str__())
#key_str_list = s3i_directory.getPublicKey(receivers)
publicKeys = [Key(key_str=i) for i in publicKeys_str]
message.encrypt(publicKeys)
print(message.pgpMsg.__str__())

endpoints = ["s3ibs://"+receivers[0]]
access_token = s3i_identity_provider.get_token(TokenType.ACCESS_TOKEN)
broker = Broker(auth_form='Username/Password', username=" ", password=access_token, host="rabbitmq.s3i.vswf.dev")
broker.send(endpoints, message.pgpMsg.__str__())