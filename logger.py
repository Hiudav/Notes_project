import pandas as pd
import json
import datetime

def Notes_create():
    with open("Notes.json","a") as file:
        json_dict = {"text": str(input("Введите заметку: ")),"date": str(datetime.datetime.now())}
        json_serial=json.dumps(json_dict)
        file.write(json_serial+"\n")

def Notes_choose():
    pass

def Notes_edit():
    pass

def Notes_remove():
    pass

def Notes_between_date():
    pass

def Notes_show():
    with open("Notes.json","r") as file:
        for line in file.readlines():
            print(line,end="")

def Notes_read():
    pass
