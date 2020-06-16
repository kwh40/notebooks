import time


def print_with_timestamp(msg):
    print(
        "[S3I][{}]: {}".format(
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg
        )
    )


def check_message_encryption(msg):
    switcher = {
        # "pgp": "-",  # ----BEGIN PGP MESSAGE-----",
        # "error": "<",  #!DOCTYPE HTML PUBLIC \"-//W", #<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"><title>500 Internal Server Error</title><h1>Internal Server Error</h1><p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>
        # "s3iMsg": "{",
        "-": "pgp",
        "<": "error",
        "{": "msg",
    }
    return switcher.get(msg[1], "error")
