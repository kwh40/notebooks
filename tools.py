import time
import logging
logging.basicConfig(level=logging.ERROR)

yes = ["j", "ja", "Ja", "J" "Yes", "y", "yes", "Y"]
no = ["n", "no", "No", "N", "nein", "Nein"]

def print_with_timestamp(msg):
    print(
        "[S3I][{}]: {}".format(
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg
        )
    )

def error_callback(message):
    logging.debug(
        "[S3I][{}]: {}".format(
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), message
        ))
    logging.debug("==============================================================================")

def check_message_encryption(msg):
    switcher = {
        "-": "pgp",
        "{": "msg",
    }
    return switcher.get(msg[1], "error")

def check_for_quotes(message):
    if message[0] == '"' and message[-1] == '"':
        return message.strip('"')
    return message


