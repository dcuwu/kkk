import time
from tkinter import messagebox

g = 0

print("[1]blik [2]karta [3]gotówka")



x = input("podaj  metode: ")

if "3" in x:
    print("gotówka")
    y = input("podaj  kwotwe: ")


if "1" in x:
    print("podaj kod blik")
    g = input("")

if "2" in x:
    print("karta")

if "6" in g:
    time.sleep(10)
    print("zatwierdzono")
else:
    messagebox.showwarning("sorry bro", ".")
    g = input("")
