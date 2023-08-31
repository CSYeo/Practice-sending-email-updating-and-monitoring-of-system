#!/usr/bin/env python3

from PIL import Image
import os

path = "{}/supplier-data/images".format(os.getcwd())
size = (600,400)

def changeImage():
  new_photos = []
  for photo in os.listdir(path):
    if photo != "README" and photo != "LICENSE":
      im = Image.open("{}/{}".format(path,photo))
      im = im.resize(size)
      im = im.convert('RGB')
      new_path = os.path.splitext("{}/{}".format(path,photo))[0]
#splitext for split extension not splittext
      im.save("{}.jpeg".format(new_path), "JPEG")
      new_photos.append("{}.jpeg".format(new_path))
  return new_photos

def main():
  changeImage()

main()
