from logger import *

def interface():
    print('Вас приветствует бот "Заметки"! Что бы вы сегодня хотели?:\
          \n 1 - создать заметку\
          \n 2 - выбор и вывод заметки\
          \n 3 - изменение выбранной заметки\
          \n 4 - удаление выбранной заметки\
          \n 5 - вывод заметок во временном диапазоне\
          \n 6 - вывод всех заметок\
          \n 7 - импортировать заметки(JSON)\
          \n 8 - выход из программы')
    while True:
        command = int(input("Введите номер команды: "))

        while command not in [1,2,3,4,5,6,7,8]:
            print("Неправильный ввод")
            command = int(input("Введите число: "))

        if command ==1:
            Notes_create()
        elif command ==2:
            Notes_choose()
        elif command ==3:
            Notes_edit()
        elif command ==4:
            Notes_remove()
        elif command ==5:
            Notes_between_date()
        elif command ==6:
            Notes_show()
        elif command ==7:
            Notes_read()
        elif command ==8:
            exit()
        print('Какая следующая команда?:\
            \n 1 - создать заметку\
            \n 2 - выбор и вывод заметки\
            \n 3 - изменение выбранной заметки\
            \n 4 - удаление выбранной заметки\
            \n 5 - вывод заметок во временном диапазоне\
            \n 6 - вывод всех заметок\
            \n 7 - импортировать заметки(JSON)\
            \n 8 - выход из программы')