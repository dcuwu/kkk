import webbrowser
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
