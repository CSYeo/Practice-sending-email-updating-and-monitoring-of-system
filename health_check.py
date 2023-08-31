#!/usr/bin/env python3

import psutil
import socket
import time

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage > 80

def check_disk_space():
    disk_usage = psutil.disk_usage('/')
    return disk_usage.percent > 80

def check_memory():
    memory = psutil.virtual_memory()
    return memory.available < 500 * 1024 * 1024  # 500MB in bytes

def check_hostname_resolution():
    try:
        host_ip = socket.gethostbyname('localhost')
        return host_ip != '127.0.0.1'
    except socket.error:
        return True

def alert(message):
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = message
  body = "Please check your system and resolve the issue as soon as possible."

  message = emails.generate(sender, receiver, subject, body)
  emails.send(message)

def main():
    while True:
        if check_cpu_usage():
            print("Error - CPU usage is over 80%")
            alert("Error - CPU usage is over 80%")
        if check_disk_space():
            print("Error - Available disk space is lower than 20%")
            alert("Error - Available disk space is lower than 20%")
        if check_memory():
            print("Error - Available memory is less than 500MB")
            alert("Error - Available memory is less than 500MB")
        if check_hostname_resolution():
            print("Error - Hostname 'localhost' cannot be resolved to '127.0.0.1'")
            alert("Error - Hostname 'localhost' cannot be resolved to '127.0.0.1'")

        time.sleep(60)  # Wait for 60 seconds before checking again

if __name__ == "__main__":
    main()
