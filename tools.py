import time
import logging
logging.basicConfig(level=logging.DEBUG)

yes = ["j", "ja", "Ja", "J" "Yes", "y", "yes", "Y"]
no = ["n", "no", "No", "N", "nein", "Nein"]
participants = ["ruecker", "kopetzky", "balindt", "kaulich", "ziesak",
                "fien", "koch", "gebhard", "arboix", "user1_workshop", "user2_workshop", "user3_workshop", "wiepcke", "schluse", "rossmann"]


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
