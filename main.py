import time
import webbrowser

a = input("Podaj liczbę: ")
b = input("Podaj liczbę: ")
print(int(a) + int(b))

print("Z przecinkiem")

c = input("Podaj liczbę: ")
d = input("Podaj liczbę: ")
print(float(c) + float(d))

x = input("Od 1 do 1M: ")
print("Zmienna x to:")
print("Werble proszę")

h = 7828754855745

print("🥁🥁🥁🥁")
time.sleep(2)
print(h)

time.sleep(2)

while True:
    o = input("Czy chcesz otworzyć stronę? (y/n): ")
    if o.lower() == "y":
        webbrowser.open("https://dcuwu.github.io/mam-to/")
        print("Strona otwarta")
        break
    elif o.lower() == "n":
        print("OK, to nie.")
        break
    else:
        print("Tylko 'y' lub 'n'.")
