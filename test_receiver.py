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
    body["client_id"] = "s3i:2aafd97c-ff05-42b6-8e4d-e492330ec959"
    body["client_secret"] = "f584c77e-e0b6-4736-831b-ccf47ab23a65"
    url = "https://idp.s3i.vswf.dev/auth/realms/KWH/protocol/openid-connect/token"

    while True:

        response = requests.post(url=url, data=body, headers={"Content-Type": "application/x-www-form-urlencoded"})
        token = response.json()["access_token"]
        #print(token)
        hmi_endpoint = "s3ib://s3i:2aafd97c-ff05-42b6-8e4d-e492330ec959"
        headers = {"Authorization": "Bearer {}".format(token)}
        res = requests.get(url="https://broker.s3i.vswf.dev/{}".format(hmi_endpoint), headers=headers)
        if not(200<= res.status_code <300):
            print(res.status_code)
            print(res.text)
        time.sleep(2)

