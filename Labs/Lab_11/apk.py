from tkinter import *
from tkinter import messagebox
import mysql.connector
from collections import deque

db = mysql.connector.connect(host="localhost",user="root",passwd="",database="sql_bool_wdi")

root = Tk()
root.resizable(width=True, height=True)
root.configure(width=720, height=480)

####    DB_QUERIES  ####
def show_orders():
    sql_query = "SELECT zlecenia.nazwa, programisci.nazwisko FROM `zlecenia` "\
                "JOIN programisci ON programisci.id=zlecenia.programistaid "\
                "WHERE zlecenia.iloscKodu > 1 "
    crs = db.cursor()
    crs.execute(sql_query)
    records = crs.fetchall()

    orders = 'ZLECENIA:\n'
    for row in records:
        orders += f"● `{row[0]}` -> {row[1]}\n"

    text.insert("1.0", orders)

def show_languages():
    sql_query = "SELECT jezyki.nazwa FROM `jezyki` WHERE 1"
    crs = db.cursor()
    crs.execute(sql_query)
    records = crs.fetchall()

    langs = 'JEZYKI:\n'
    for row in records:
        langs += f"● {row[0]}\n"

    text.insert("1.0", langs)

def show_workers():
    sql_query = "SELECT programisci.imie, programisci.nazwisko FROM `programisci` WHERE 1"
    crs = db.cursor()
    crs.execute(sql_query)
    records = crs.fetchall()

    workers = 'Pracownicy:\n'
    for i in range(len(records)):
        workers += f"{i+1} -> {records[i][0]} {records[i][1]}\n"

    text.insert("1.0", workers)

def get_workers():
    sql_query = "SELECT programisci.id, programisci.nazwisko FROM `programisci` WHERE 1"
    crs = db.cursor()
    crs.execute(sql_query)
    records = sorted(crs.fetchall())

    workers_tab = []
    for row in records:
        workers_tab.append(row[0])

    return workers_tab

def show_tables():
    sql_query = "SHOW TABLES"
    crs = db.cursor()
    crs.execute(sql_query)
    records = crs.fetchall()

    tables = 'TABELE:\n'
    for row in records:
        tables += f"● {row[0]}\n"

    text.insert("1.0", tables)

def show_orders_line(line):
    sql_query = f"SELECT zlecenia.nazwa, programisci.nazwisko FROM `zlecenia` "\
                f"JOIN programisci ON programisci.id=zlecenia.programistaid "\
                f"WHERE zlecenia.iloscKodu > {line} "
    crs = db.cursor()
    crs.execute(sql_query)
    records = crs.fetchall()

    orders = f'Zlecenia, które mają ponad {line} linii kodu:\n'
    for row in records:
        orders += f"Za `{row[0]}` odpowiada {row[1]}\n"

    text.insert("1.0", orders)

def insert_order():
    progr = prog.get()
    name = en_order_name.get()
    lines = en_lines.get()

    if (progr == "" or name == "" or lines == ""):
        messagebox.showerror("Błąd wpisywania", "Wszystkie pola są wymagane!")
    else:
        sql_query = f"INSERT INTO `zlecenia` (`id`, `programistaid`, `nazwa`, `iloscKodu`)\
                    VALUES (NULL, '{progr}', '{name}', '{lines}');"
        # sql_query = "INSERT INTO `zlecenia` (`id`, `programistaid`, `nazwa`, `iloscKodu`)\
        # VALUES (NULL, '" + progr + "', '" + name + "', '" + lines + "');"
        print(sql_query)
        crs = db.cursor()
        crs.execute(sql_query) #USUNĄĆ TRUE JAK MA NIE DZIAŁAĆ DROP
        crs.execute("commit")
        messagebox.showinfo("Wpisywanie", "Wpisano dane!")
########################

####    FUNCTIONS   ####
def mouse_move(event):
    # print(event.x, event.y)
    canv.create_oval(event.x+1, event.y+1, event.x-1, event.y-1, outline='#28085f', fill='blue')

def clear_canv(event):
    # print(canv.find_all())
    list(map(lambda i : canv.delete(i), canv.find_all()))
    deque(map(lambda i : canv.delete(i), canv.find_all()))

def user_input():
    pass

def clear_text():
    text.delete("1.0", END)
########################

####    MAIN    ####
label = Label(root, text="Programik na ostatnie laby")
label.grid(row=0, column=0)

frame = Frame(root, borderwidth=3)
frame.grid(row=1,column=0)
frame.configure(background='#807fbb')

l1 = Label(frame, text="Tutaj coś podaje użytkownik")
l1.grid(sticky=N, row=0, column=0, padx=5, pady=5)
l1.configure(background='#807fbb')

entry = Entry(frame, width=67)
entry.grid(sticky=W, row=1, column=0,padx=5,pady=5)

btn_frame = Frame(frame, borderwidth=3)
btn_frame.grid(row=2, column=0)
btn_frame.configure(background='#807fbb')

btn = Button(btn_frame, text="Tabele", command=show_tables)
btn.grid(sticky=W, row=0, column=0)
btn.configure(background='#cca4c5', foreground='#28085f')

btn2 = Button(btn_frame, text="Zlecenia", command=show_orders)
btn2.grid(sticky=W, row=0, column=1)
btn2.configure(background='#cca4c5', foreground='#28085f')

btn3 = Button(btn_frame, text="Języki", command=show_languages)
btn3.grid(sticky=W, row=0, column=2)
btn3.configure(background='#cca4c5', foreground='#28085f')

btn3 = Button(btn_frame, text="Pracownicy", command=show_workers)
btn3.grid(sticky=W, row=0, column=3)
btn3.configure(background='#cca4c5', foreground='#28085f')

btn5 = Button(btn_frame, text="Czyść tekst", command=clear_text)
btn5.grid(sticky=W, row=0, column=4)
btn5.configure(background='#cca4c5', foreground='#28085f')

canv = Canvas(frame, width=400, height=50)
canv.bind('<B1-Motion>', mouse_move)
canv.bind('<Button-3>', clear_canv)
canv.grid(sticky=S, row=3, column=0,padx=5, pady=5)
canv.configure(background="#807fbb")

text = Text(frame, width=50, height=10)
text.grid(sticky=W+N, row=4,column=0,padx=5,pady=5)

## ADDING RECORDS ##
frame_right = Frame(root, borderwidth=3)
frame_right.grid(sticky=N, row=1, column=1)
frame_right.configure(background='#807fbb')

l21 = Label(root, text="Dodawanie zleceń")
l21.grid(sticky=N, row=0, column=1)

programmer = Label(frame_right, text="Programista: ")
programmer.grid(sticky=E, row=1, column=0, padx=5, pady=5)
programmer.configure(background='#807fbb')
OPTIONS = get_workers()
prog = StringVar(frame_right)
prog.set(OPTIONS[0])
en_progr = OptionMenu(frame_right, prog, *OPTIONS)
en_progr.grid(sticky=W, row=1, column=1)

order_name = Label(frame_right, text="Nazwa: ")
order_name.grid(sticky=E, row=2, column=0, padx=5, pady=5)
order_name.configure(background='#807fbb')
en_order_name = Entry(frame_right, width= 30)
en_order_name.grid(sticky=W, row=2, column=1, padx=5, pady=5)

lines = Label(frame_right, text="Ile kodu: ")
lines.grid(sticky=E, row=3, column=0, padx=5, pady=5)
lines.configure(background='#807fbb')
en_lines = Entry(frame_right, width= 30)
en_lines.grid(sticky=W, row=3, column=1, padx=5, pady=5)

btn = Button(frame_right, text="Dodaj zlecenie", command=insert_order)
btn.grid(sticky=N, row=4, column=0)
btn.configure(background='#cca4c5', foreground='#28085f')

canvr = Canvas(frame_right, width=270, height=207)
canvr.grid(row=5, columnspan=2)
img = PhotoImage(file="Lab_11\oberiba.png")
canvr.create_image(-10,10, anchor=NW ,image=img)
###################

root.mainloop()
db.close()