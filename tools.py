import time


def print_with_timestamp(msg):
    print(
        "[S3I][{}]: {}".format(
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg
        )
    )

def error_callback(message):
    print("An Error occured:", message)
    print("==============================================================================")

def check_message_encryption(msg):
    switcher = {
        "-": "pgp",
        "{": "msg",
    }
    return switcher.get(msg[1], "error")
