#!/usr/bin/env python3

from PIL import Image
import os

path = "{}/supplier-data/images".format(os.getcwd())
size = (128,128)

def changeImage():
  new_photos = []
  for photo in os.listdir(path):
    if photo != README:
      im = Image.open("{}/{}".format(path,photo))
      im = im.rotate(270).resize(size)
      im = im.convert('RGB')
      new_path = os.path.splittext("{}/{}".format(path,photo))[0]
      im.save("{}.jpeg".format(new_path), "JPEG")
      new_photos.append("{}.jpeg".format(new_path))
  return new_photos

def main():
  changeImage()

main()
