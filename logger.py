import pandas as pd
import json
import datetime

def Notes_create():
    with open(r"Notes.json","r") as file:
        lines=sum(1 for line in file)+1
    with open("Notes.json","a+") as file:
        now=datetime.datetime.now()
        json_dict = {"id": int(lines),"title": str(input("Введите заголовок: ")), "text": str(input("Введите заметку: ")),"date": str("{}.{}.{}".format(now.day,now.month,now.year))}
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
    with open("Notes.json","r") as file:
        if_t=False
        edit_file=list(file.readlines())
        choose_id=int(input("Введите id выбранной заметки: "))
        for i in range(0,len(edit_file)):
                if json.loads(edit_file[i].strip("\n"))["id"]==choose_id:
                    json_dict=json.loads(edit_file[i].strip("\n"))
                    print("Изменяемая заметка: ")
                    print(json.loads(edit_file[i].strip("\n")))
                    new_title=str(input("Введите новый заголовок: "))
                    json_dict["title"]=new_title
                    new_note=str(input("Введите новую заметку: "))
                    json_dict["text"]=new_note
                    edit_file[i]=f'{json.dumps(json_dict)}\n'
                    if_t=True
                    break
        else:
            print("Не нашёл такой заметки ")
    if if_t==True:
        with open("Notes.json","w") as file:
            file.writelines(edit_file)

def Notes_remove():
    with open("Notes.json","r") as file:
        if_t=False
        edit_file=[]
        choose_id=int(input("Введите id выбранной заметки: "))
        for line in file:
                if json.loads(line.strip("\n"))["id"]==choose_id:
                    print("Удалённая заметка: ")
                    print(json.loads(line.strip("\n")))
                    if_t=True
                else:
                    edit_file.append(line)
        if if_t==True:
            with open("Notes.json","w") as file:
                file.writelines(edit_file)
        else:
            print("Не нашёл такой заметки ")
    

def Notes_between_date():
    with open("Notes.json","r") as file:
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
    with open("Notes.json","a") as file:
        with open(str(input('Формат JSON: {"id": id, "title": "title", "text": "text", "date": "dd.mm.yyyy"}\nВведите путь к импортируемуму JSON: \n')),"r") as file_import:
            file.writelines(file_import.readlines())
