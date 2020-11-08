import time
import logging
logging.basicConfig(level=logging.ERROR)

yes = ["j", "ja", "Ja", "J" "Yes", "y", "yes", "Y"]
no = ["n", "no", "No", "N", "nein", "Nein"]
up = ["u", "U", "up", "Up", "ShieldUp", "shieldUp", "shieldup", "Shieldup"]
down = ["d", "D", "down", "Down", "ShieldDown",
        "shieldDown", "shielddown", "Shielddown"]

configuration_app_id = "s3i:a44bd6dc-c607-4574-9b16-cf8579819356"
configuration_app_secret = "970ebe57-7dfb-4090-8c38-4b44111d5288"

def print_with_timestamp(msg):
    print(
        "[S3I][{}]: {}".format(
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg
        )
    )


def error_callback(message):
    logging.debug(
        "[S3I][{}]: {}".format(
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()
                          ), "An error occurred"
        ))
    logging.debug(
        "[S3I][{}]: {}".format(
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), message
        ))
    logging.debug(
        "==============================================================================")


def check_message_encryption(msg):
    switcher = {
        "-": "pgp",
        "{": "msg",
    }
    return switcher.get(msg[0], "error")


def check_for_quotes(message):
    return message.strip('," ')


def check_for_spaces(text):
    return text.strip('," ')
