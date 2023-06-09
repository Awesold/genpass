from tkinter import *
import string, random

root = Tk()
root.geometry("500x500")
root.title("Генератор паролей")

upper, lower = string.ascii_uppercase, string.ascii_lowercase
punctuation, digits = string.punctuation, string.digits
chars, length_password, password = digits, '', ''


def get_grid(quest, widget, symb, q, b1, b2):
    global question, length_pass, button1, button2, length_button
    question = Label(text=quest)
    symbol = symb
    button1 = Button(text="да", command=lambda: answ('да', symb))
    button2 = Button(text="нет", command=lambda: answ('нет', 0))
    length_pass = Entry()
    length_button = Button(text="ок", command=lambda: answ('ок', length_pass.get()))

    if widget == 'Вопрос':
        question.grid(row=q[0], column=q[1], columnspan=q[2])
        button1.grid(row=b1[0], column=b1[1], columnspan=b1[2])
        button2.grid(row=b2[0], column=b2[1], columnspan=b2[2])

    elif widget == 'Длина':
        question.grid(row=q[0], column=q[1], columnspan=q[2])
        length_pass.grid(row=b1[0], column=b1[1], columnspan=b1[2])
        length_button.grid(row=b2[0], column=b2[1], columnspan=b2[2])

    elif widget == 'Генерация':
        length_button = Button(text="Сгенерировать пароль", command=lambda: answ('ген', 0))
        length_button.grid(row=q[0], column=q[1], columnspan=q[2])

    elif widget == 'Сохранение':
        question.grid(row=q[0], column=q[1], columnspan=q[2])
        button1.grid(row=b1[0], column=b1[1], columnspan=b1[2])
        button2.grid(row=b2[0], column=b2[1], columnspan=b2[2])


def forget_grid(widget):
    global question, length_pass, button1, button2, length_button
    if widget == 'Вопрос':
        question.grid_forget()
        button1.grid_forget()
        button2.grid_forget()

    elif widget == 'Длина':
        question.grid_forget()
        length_pass.grid_forget()
        length_button.grid_forget()
    elif widget == 'Генерация':
        length_button.grid_forget()


def answ(ans, symbol):
    global chars, event, length_password, password
    if ans == 'да':
        if event == 6:
            file = open("пароли.txt", "w")
            file.write(password)
            file.close()
            question['text'] = 'Сохранено!'
            event = 6
        else:
            chars += symbol
        event += 1
        update(event)

    if ans == 'нет':
        if event == 6:
            question['text'] = 'Не сохранено!'
        event += 1
        update(event)

    if ans == 'ок':
        length_password = int(symbol)
        event += 1
        update(event)

    if ans == 'ген':
        password = ''.join([random.choice(chars) for _ in range(length_password)])
        event = 6
        update(event)


def update(event):
    if event == 1:
        get_grid("Выберите длину пароля: ", 'Длина', 0, [1, 2, 6], [2, 3, 1], [2, 6, 1])

    if event == 2:
        forget_grid('Длина')
        get_grid("Пароль будет содержать прописные буквы?", 'Вопрос', lower, [1, 2, 6], [2, 3, 1], [2, 6, 1])

    if event == 3:
        forget_grid('Вопрос')
        get_grid("Пароль будет содержать заглавные буквы?", 'Вопрос', upper, [1, 2, 6], [2, 3, 1], [2, 6, 1])

    if event == 4:
        forget_grid('Вопрос')
        get_grid("Будет ли пароль содержать символы?", 'Вопрос', punctuation, [1, 2, 6], [2, 3, 1], [2, 6, 1])

    if event == 5:
        forget_grid('Вопрос')
        get_grid('', 'Генерация', 0, [1, 2, 6], [2, 3, 1], [2, 6, 1])
    if event == 6:
        forget_grid('Вопрос')
        get_grid(f"Ваш пароль - {password}\nСохранить пароль в файл (да/нет)? ", 'Вопрос', 'save', [2, 2, 6], [3, 3, 1],
                 [3, 6, 1])
    if event == 7:
        forget_grid('Вопрос')
        question.grid(row=2, column=2, columnspan=6)


text = Label(text="Чтобы создать пароль нужно выбрать его длину и ответить на несколько вопросов")
text.grid(columnspan=10)
event = 1
update(event)
root.mainloop()