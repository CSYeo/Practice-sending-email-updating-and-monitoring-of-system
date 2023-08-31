#!/usr/bin/env python3
import os
import datetime
import reports

folder = "{}/supplier-data/descriptions".format(os.getcwd())

def report(f):
  name_weight = ""
  for txt in os.listdir(f):
    filepath = "{}/{}".format(f, txt)

        with open(filepath, 'r') as data:
            lines = data.readlines()
    #lines now will read one line at a time
            name&weight = "{}\n"lines[0:1].strip()
            name_weight = name_weight.join(name&weight)
  return name_weight
