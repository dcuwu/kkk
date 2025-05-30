import tkinter as tk

class Klikacz:
    def __init__(self, master):
        self.master = master
        master.title("Klikacz")

        self.liczba_klikniec = 100000000000000000000000000000000000000000

        self.label = tk.Label(master, text="Kliknij przycisk!")
        self.label.pack()

        self.kliknij_przycisk = tk.Button(master, text="Kliknij mnie!", command=self.zlicz_klikniecia)
        self.kliknij_przycisk.pack()

        self.wynik_label = tk.Label(master, text="Liczba kliknięć: 0")
        self.wynik_label.pack()

        self.zapisz_przycisk = tk.Button(master, text="Zapisz wynik", command=self.zapisz_wynik)
        self.zapisz_przycisk.pack()

    def zlicz_klikniecia(self):
        self.liczba_klikniec +=100000000000000000000000000000000000000000
        self.wynik_label.config(text=f"Liczba kliknięć: {self.liczba_klikniec}")

    def zapisz_wynik(self):
        with open("winik.txt", "w") as plik:
            plik.write(f"Liczba kliknięć: {self.liczba_klikniec}")
        self.wynik_label.config(text="Wynik zapisany do 'wynik.txt'")

if __name__ == "__main__":
    root = tk.Tk()
    klikacz = Klikacz(root)
    root.mainloop()
