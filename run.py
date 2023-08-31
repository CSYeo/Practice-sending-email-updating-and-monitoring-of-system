
#! /usr/bin/env python3

import os
import requests

directory = "{}/data/descriptions".format(os.getcwd())

def parse(folder):
    posts = []

    for file in os.listdir(folder):
        #print(file)
        #Here remember to use os.listdir if not it will
        #print directory as a string

        filepath = "{}\\{}".format(folder, file)

        with open(filepath, 'r') as data:
            lines = data.readlines()
    #lines now will read one line at a time
            name = lines[0].strip()
            weight = lines[1].strip()
            description = ''.join(lines[2:]).strip()

            dict = {
            "name": name,
            "weight (in lbs)": weight,
            "description": description,
            }

        posts.append(dict)

    return posts

to_post = parse(directory)

for p in to_post:
    response = requests.post("https://http://34.74.64.240/fruits/", data=p)
    print(response)
    #here any action would do, we just need to call the response
