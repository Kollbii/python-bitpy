import tkinter as tk
import random
import re
from tkinter import ttk

root = tk.Tk()
root.geometry('780x300')




def clear_board():
    t.delete("1.0","end")

def indexes_of_0(stringArr):
    indexes = []
    for i in range(0, len(stringArr)):
        if stringArr[i] == '0':
            indexes.append(i)
    return indexes

def take_out(givenString, stringArr, g): 
    final = g
    takenOut = re.search(('0(.+?)0'), givenString)
    indexes = indexes_of_0(stringArr)

    if takenOut != None:
        takenOut = re.search(('0(.+?)0'), givenString).group(1)
        for i in range (0, len(takenOut)):
            if ord(takenOut[i]) == 48:
                newString = givenString[indexes[1]:]
                newArr = list(newString)
                return take_out(newString, newArr, final)
        final += ''.join(takenOut)
        newString = givenString[indexes[1]:]
        newArr = list(newString)
        return take_out(newString, newArr, final)
    else:
        return final

def gener_string():
    randString = ""

    for _ in range (random.randint(10, 50)):
        zeroChance = random.randint(1, 10)
        char = random.randint(48, 122)
        if zeroChance == 1:
            randString += ''.join('0')
        else:
            randString += ''.join(chr(char))

    fs = randString
    randString += ''.join("\n")
    t.insert(tk.END, randString)

    return fs

def start():
    givenString = gener_string()
    a = re.search(('0(.+?)0'), givenString)
    if(a):
        stringArr = list(givenString)
        final = take_out(givenString, stringArr, '')
        t.insert(tk.END, "String z wyciągniętymi zerami: ")
        t.insert(tk.END, final)
        t.insert(tk.END, "\n\n")
        return final
    else:
        t.insert(tk.END, "Podano jedno lub żadnych zer\n")
        t.insert(tk.END, "\n")
        return "Podano jedno lub żadnych zer\n"



t = tk.Text(root)

scroll = tk.Scrollbar(root, orient=tk.VERTICAL, command=t.yview)
scroll.pack(side=tk.RIGHT, expand=True, fill=tk.Y)
t.pack(side=tk.RIGHT, expand=True)
t.configure(yscrollcommand=scroll.set)

b = tk.Button(root, text='Gener string', command=start)
b.pack(side=tk.LEFT)
c = tk.Button(root, text='Clear', command=clear_board)
c.pack(side=tk.LEFT)


# style = ttk.Style()
# style.theme_use('clam')
root.mainloop()