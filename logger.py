import pandas as pd
import json
import datetime

def Notes_create():
    with open(r"Notes.json","r") as file:
        lines=sum(1 for line in file)+1
    with open("Notes.json","a+") as file:
        now=datetime.datetime.now()
        json_dict = {"id": int(lines),"text": str(input("Введите заметку: ")),"date": str("{}.{}.{}".format(now.day,now.month,now.year))}
        json_serial=json.dumps(json_dict)
        file.write(json_serial+"\n")

def Notes_choose():
    with open("Notes.json","r") as file:
        choose_id=int(input("Введите id выбранной заметки: "))
        for line in file:
            if json.loads(line.strip("\n"))["id"]==choose_id:
                print(json.loads(line.strip("\n")))
                break
        else:
            print("Не нашёл такой заметки ")

def Notes_edit():
    pass

def Notes_remove():
    pass

def Notes_between_date():
    with open("Notes_done.json","r") as file:
            data=[json.loads(x.strip("\n")) for x in file]
            df=pd.DataFrame(data)
            while True:
                try:
                    date_before=datetime.datetime.strptime(str(input("\033[37mВведите начало временного диапазона(dd.mm.yy): ")),"%d.%m.%Y")
                    date_after=datetime.datetime.strptime(str(input("Введите конец временного диапазона(dd.mm.yy): ")),"%d.%m.%Y")
                    break
                except ValueError:
                    print("\033[31mВы ввели неверный формат даты. Повторите попытку")
            print(df[(df["date"].apply(lambda s: datetime.datetime.strptime(s,"%d.%m.%Y"))<=date_after) & 
                    (date_before<=df["date"].apply(lambda s: datetime.datetime.strptime(s,"%d.%m.%Y")))])

def Notes_show():
    with open("Notes.json","r") as file:
        data=[json.loads(x.strip("\n")) for x in file]
        df=pd.DataFrame(data)
        print(df)

def Notes_read():
    pass
