import time

def print_with_timestamp(msg):
    print("[S3I][{}]: {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg))