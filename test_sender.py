import requests
import json
import time

if __name__ == "__main__":
    username = "KWH-Team"
    password = "V4yuJ31izh0GCH36954O"
    body = dict()
    body["username"] = username
    body["password"] = password
    body["grant_type"] = "password"
    body["client_id"] = "s3i:6f58e045-fd30-496d-b519-a0b966f1ab01"
    body["client_secret"] = "475431fd-2c6d-4cae-bdfa-87226fff0cef"
    url = "https://idp.s3i.vswf.dev/auth/realms/KWH/protocol/openid-connect/token"

    while True:
        response = requests.post(url=url, data=body, headers={"Content-Type": "application/x-www-form-urlencoded"})
        token = response.json()["access_token"]
        #print(token)
        receiver_endpoint = "s3ib://s3i:2aafd97c-ff05-42b6-8e4d-e492330ec959"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer {}".format(token)}
        data = {
                 "sender": "s3i:6f58e045-fd30-496d-b519-a0b966f1ab01",
                 "identifier": "s3i:1385e09e-3e93-4c2f-92d3-345698c40407",
                 "receivers": ["s3i:2aafd97c-ff05-42b6-8e4d-e492330ec959"],
                 "messageType": "userMessage",
                 "replyToEndpoint": "s3ibs://s3i:6f58e045-fd30-496d-b519-a0b966f1ab01",
                 "attachments": [],
                 "subject": "subject of message",
                 "text": "Dear Mr. Example, ..."
                }
        res = requests.post(url="https://broker.s3i.vswf.dev/{}".format(receiver_endpoint), data=json.dumps(data), headers=headers)
        print(res.status_code)
        print(res.text)
        time.sleep(2)

