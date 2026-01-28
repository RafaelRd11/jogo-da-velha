import tkinter as tk  # importa a biblioteca do Tkinter pra criar janelas e botões
from tkinter import messagebox  # importa só pra mostrar aquelas janelinhas de alerta

janela = tk.Tk()  # cria a janela principal
janela.title("jogo")  # coloca o título da janela
janela.geometry("800x1000")  # define o tamanho da janela (largura x altura)

vez = "X"  # começa com o X
tab = ["", "", "", "", "", "", "", "", ""]  # lista que guarda o que cada quadrado tem
bts = []  # lista pra guardar os botões depois

texto = tk.Label(janela, text="Vez do: X", font=("Arial", 20))  # um texto que mostra de quem é a vez
texto.pack()  # coloca o texto na janela

quadro = tk.Label(janela)  # cria um espaço pra colocar os botões
quadro.pack()  # coloca esse espaço na janela

# função que verifica se alguém ganhou
def ganhou():
    if tab[0] == tab[1] == tab[2] != "":  # primeira linha
        return True
    if tab[3] == tab[4] == tab[5] != "":  # segunda linha
        return True
    if tab[6] == tab[7] == tab[8] != "":  # terceira linha
        return True
    if tab[0] == tab[3] == tab[6] != "":  # primeira coluna
        return True
    if tab[1] == tab[4] == tab[7] != "":  # segunda coluna
        return True
    if tab[2] == tab[5] == tab[8] != "":  # terceira coluna
        return True
    if tab[0] == tab[4] == tab[8] != "":  # diagonal principal
        return True
    if tab[2] == tab[4] == tab[6] != "":  # diagonal inversa
        return True
    return False  # se não tiver nenhuma das anteriores, ninguém ganhou ainda

# função que reinicia o jogo
def resetar():
    global vez  # fala que vamos mexer na variável global vez
    vez = "X"  # sempre começa com X de novo
    texto.config(text="Vez do: X")  # atualiza o texto da vez
    for i in range(9):  # vai limpar todos os quadrados
        tab[i] = ""  # tira o X ou O do tabuleiro
        bts[i].config(text="")  # tira o texto do botão

# função que acontece quando clica num botão
def clicar(n):
    global vez  # de novo, mexe na variável vez
    if tab[n] != "":  # se o quadrado já tiver alguma coisa, não faz nada
        return

    tab[n] = vez  # coloca o X ou O na posição
    bts[n].config(text=vez)  # mostra no botão

    if ganhou():  # se alguém ganhou
        messagebox.showinfo("fim", vez + " ganhou")  # mostra mensagem
        resetar()  # reinicia o jogo
        return

    if "" not in tab:  # se todos os quadrados estão cheios e ninguém ganhou
        messagebox.showwarning("empate", "deu velha")  # mostra que deu empate
        resetar()  # reinicia o jogo
        return

    if vez == "X":  # troca a vez
        vez = "O"
    else:
        vez = "X"

    texto.config(text="Vez do: " + vez)  # atualiza o texto da vez

# cria os 9 botões do jogo
for i in range(9):
    bt = tk.Button(quadro, text="", width=5, height=2, font=("Arial", 30))  # cria botão
    bt.config(command=lambda x=i: clicar(x))  # fala que quando clicar chama a função clicar
    bt.grid(row=i//3, column=i%3)  # organiza o botão na tabela 3x3
    bts.append(bt)  # adiciona o botão na lista

# botão pra reiniciar manualmente
botao = tk.Button(janela, text="reiniciar", command=resetar)
botao.pack()

janela.mainloop()  # roda o programa, abre a janela
