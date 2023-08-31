#! /usr/bin/env python3

import os
import requests

directory = "{}\\data\\feedback".format(os.getcwd())

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
            title = lines[0].strip()
            name = lines[1].strip()
            date = lines[2].strip()
            feedback = ''.join(lines[3:]).strip()

            dict = {
            "title": title,
            "name": name,
            "date": date,
            "feedback": feedback
            }

        posts.append(dict)

    return posts

to_post = parse(directory)

for p in to_post:
    response = requests.post("https://example.com/path/to/api", data=p)
    print(response)
    #here any action would do, we just need to call the response
