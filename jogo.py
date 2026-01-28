import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("jogo")
janela.geometry("800x1000")

vez = "X"
tab = ["", "", "", "", "", "", "", "", ""]
bts = []

texto = tk.Label(janela, text="Vez do: X", font=("Arial", 20))
texto.pack()

quadro = tk.Label(janela)
quadro.pack()

def ganhou():
    if tab[0] == tab[1] == tab[2] != "":
        return True
    if tab[3] == tab[4] == tab[5] != "":
        return True
    if tab[6] == tab[7] == tab[8] != "":
        return True
    if tab[0] == tab[3] == tab[6] != "":
        return True
    if tab[1] == tab[4] == tab[7] != "":
        return True
    if tab[2] == tab[5] == tab[8] != "":
        return True
    if tab[0] == tab[4] == tab[8] != "":
        return True
    if tab[2] == tab[4] == tab[6] != "":
        return True
    return False

def resetar():
    global vez
    vez = "X"
    texto.config(text="Vez do: X")
    for i in range(9):
        tab[i] = ""
        bts[i].config(text="")

def clicar(n):
    global vez
    if tab[n] != "":
        return

    tab[n] = vez
    bts[n].config(text=vez)

    if ganhou():
        messagebox.showinfo("fim", vez + " ganhou")
        resetar()
        return

    if "" not in tab:
        messagebox.showwarning("empate", "deu velha")
        resetar()
        return

    if vez == "X":
        vez = "O"
    else:
        vez = "X"

    texto.config(text="Vez do: " + vez)

for i in range(9):
    bt = tk.Button(quadro, text="", width=5, height=2, font=("Arial", 30))
    bt.config(command=lambda x=i: clicar(x))
    bt.grid(row=i//3, column=i%3)
    bts.append(bt)

botao = tk.Button(janela, text="reiniciar", command=resetar)
botao.pack()

janela.mainloop()
