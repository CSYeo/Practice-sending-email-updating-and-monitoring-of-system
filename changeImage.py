#!/usr/bin/env python3

from PIL import Image
import os

path = os.getcwd()
size = (128,128)

for photo in os.listdir("~/supplier-data/images"):
    im = Image.open("{}/images/{}".format(path,photo))
    im = im.rotate(270).resize(size)
    im = im.convert('RGB')
    im.save("{}/images/{}.jpeg".format(path,photo), "JPEG")
