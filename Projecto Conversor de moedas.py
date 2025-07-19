from tkinter.ttk import *
from tkinter import *

janela = Tk()
janela.title("App Conversor de Temperatura")
janela.config(bg = "black")
janela.geometry("530x300")
janela.resizable(width=True, height=True)

temperaturas = ["Graus Célcios", "Faraday", "Kelvin"]

def obter_lista_1():
    obter_1 = entry_lista1.get()
    label_1 ["text"] = obter_1
    label_1 ["fg"] = "blue"
    celcius = (5/9) * (obter_1 - 32)
    
def obter_lista_2():
    obter_2 = entry_lista2.get()
    label_2 ["text"] = obter_2
    label_2 ["fg"] = "blue"

  

label_tema = Label(janela, width=30, height=2, text = "Conversor de Temperatura", fg = "yellow", relief = "solid", bg = "black", font = "Algerian 15")
label_tema.place(x = 70, y = 1)

label_principal = Label(janela, width=30, height=1, font = "Arial 15 bold", bg = "black", fg = "red", text = "- - - - - - - -")
label_principal.place(x=73, y=55)

entry_lista1 = Entry (janela, width=11, bg = "white", fg = "black", font = "Arial 10")
entry_lista1.place(x=86, y=100)

entry_lista2 = Entry (janela, width=11, bg = "white", fg = "black", font = "Arial 10")
entry_lista2.place(x=360, y=100)

combo_lista1 = Combobox(janela, width=11, height=1, font="Times 12")
combo_lista1.place(x=10, y=130)
combo_lista1 ["values"] = temperaturas
combo_lista1.current(0)

label_1 = Label (janela, text = " - - - - ", width=13, height=1, bg = "white", fg = "red", font="calibri 10", anchor="center")
label_1.place(x=130, y=130)

botao_1 = Button(janela, width=10, text = "ENTER", command=obter_lista_1)
botao_1.place(x=88, y=160)

label_para = Label (janela, text="para", width=5, height=1, bg = "black", fg = "white", font="Arial 12")
label_para.place(x=230, y=130)

combo_lista2 = Combobox(janela, width=11, height=1, font="Times 12")
combo_lista2.place(x=280, y=130)
combo_lista2 ["values"] = temperaturas
combo_lista2.current(0)

label_2 = Label (janela, text = " - - - - ", width=13, height=1, bg = "white", fg = "red", font="calibri 10")
label_2.place(x=400, y=130)

botao_2 = Button(janela, width=10, text = "ENTER", command=obter_lista_2)
botao_2.place(x=360, y=160)


botao_3 = Button(janela, width=25, text = "Converter")
botao_3.place(x=170, y=230)





janela.mainloop()

