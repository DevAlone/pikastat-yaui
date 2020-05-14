#!/usr/bin/env python3

import json
import random
import string
from os import listdir
from os.path import isfile

filenames = [f for f in listdir("./") if isfile(f) and f.endswith(".json")]

for filename in filenames:
    with open(filename, "r") as file:
        data = file.read()

    json_data = json.loads(data)
    for i in range(len(json_data)):
        json_data[i]["pikabu_id"] = random.randint(1, 2 ** 64)
        json_data[i]["parent_id"] = random.randint(1, 2 ** 64)
        json_data[i]["created_at_timestamp"] = random.randint(1, 2 ** 64)
        json_data[i]["story_id"] = random.randint(1, 2 ** 64)
        json_data[i]["story_url"] = "https://pikabu.ru/story/_58"
        json_data[i]["story_title"] = "заголовок"
        json_data[i]["story_title"] = "заголовок"

        text = json_data[i]["text"]
        new_text = ""
        for character in text:
            if random.random() < 0.25:
                new_text += random.choice(string.ascii_letters)
            else:
                new_text += character

        json_data[i]["text"] = new_text

    with open(filename, "w") as file:
        file.write(json.dumps(json_data))
