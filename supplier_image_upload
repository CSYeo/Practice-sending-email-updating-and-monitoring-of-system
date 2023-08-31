#!/usr/bin/env python3
import requests
import changeImage

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
for photo in changeImage.changeImage():
  with open(photo, 'rb') as opened:
    r = requests.post(url, files={'file': opened})
