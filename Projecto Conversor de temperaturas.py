from tkinter.ttk import *
from tkinter import *

janela = Tk()
janela.title("App Conversor de Temperatura")
janela.config(bg = "black") 
janela.geometry("530x300")
janela.resizable(width=True, height=True)

temperaturas = ["Graus Célcios", "Faraday", "Kelvin"]


def converter():
    try:
        dados_inicial = float(entry_lista1.get())
        dados_origem = combo_lista1.get()
        dados_destino = combo_lista2.get()

        valor_convertido = 0

        # Converter para Celsius primeiro, pois é a unidade base para as outras conversões
        if dados_origem == "Graus Célcios":
            valor_celsius = dados_inicial
        elif dados_origem == "Faraday":
            # Fórmula de Faraday para Celsius: C = (5/9) * (F - 32)
            valor_celsius = (5/9) * (dados_inicial - 32)
            if valor_celsius < 0:
                label_clima.config(text = "Esta Muito Frio", fg = "blue")
            if valor_celsius > 1 and valor_celsius < 9:
                label_clima.config(text = "Está Frio", fg = "blue")
            if valor_celsius == 10 and valor_celsius < 19:
                label_clima.config(text = "Clima Fresco", fg = "blue")
            if valor_celsius >= 20 and valor_celsius < 24:
                label_clima.config(text = "Clima Agradável", fg = "blue")
            if valor_celsius >= 25 and valor_celsius < 30:
                label_clima.config(text = "Clima Quente", fg = "blue")
            else:
                label_clima.config(text = "Clima Muito Quente", fg = "blue")

        elif dados_origem == "Kelvin":
            # Fórmula de Kelvin para Celsius: C = K - 273.15
            valor_celsius = dados_inicial - 273.15
            
            if valor_celsius < 0:
                label_clima.config(text = "Clima Muito Frio", fg = "blue")
            if valor_celsius > 1 and valor_celsius < 14:
                label_clima.config(text = "Clima Frio", fg = "blue")
            if valor_celsius >= 15 and valor_celsius < 24:
                label_clima.config(text = "Clima Confortável", fg = "blue")
            if valor_celsius >= 25 and valor_celsius < 35:
                label_clima.config(text = "Clima Quente", fg = "blue")
            else:
                label_clima.config(text = "Clima Muito Quente", fg = "blue")
        else:
            label_principal.config(text="Unidade inválida", fg="red")
            return
        
        # Converter de Celsius para a unidade de destino
        if dados_destino == "Graus Célcios":
            valor_convertido = valor_celsius
        elif dados_destino == "Faraday":
            # Fórmula de Celsius para Faraday: F = (9/5) * C + 32
            valor_convertido = (9/5) * valor_celsius + 32
            if valor_convertido < 32:
                label_clima.config(text = "Clima Muito Frio", fg = "blue")
            if valor_convertido > 33 and valor_convertido < 49:
                label_clima.config(text = "Clima Frio", fg = "blue")
            if valor_convertido >= 50 and valor_convertido < 76:
                label_clima.config(text = "Clima Agradável", fg = "blue")
            if valor_convertido >= 77 and valor_convertido < 95:
                label_clima.config(text = "Clima Quente", fg = "blue")
            else:
                label_clima.config(text = "Clima Muito Quente", fg = "blue")

        elif dados_destino == "Kelvin":
            # Fórmula de Celsius para Kelvin: K = C + 273.15
            valor_convertido = valor_celsius + 273.15
            if valor_convertido < 10:
                label_clima.config(text = "Clima Muito Frio", fg = "blue")
        else:
            label_principal.config(text="Unidade inválida", fg="red")
            return

        # Atualizar o label_principal com o resultado
        label_principal.config(text=f"{valor_convertido:.2f}", fg="yellow") # Formata para 2 casas decimais

    except ValueError:
        label_principal.config(text="Valor inválido", fg="red")
    except Exception as e:
        label_principal.config(text=f"Erro: {e}", fg="red")

# Criação do painel informativo do tema "Conversor de temperaturas" 
label_tema = Label(janela, width=30, height=2, text = "Conversor de Temperatura", fg = "yellow", relief = "solid", bg = "black", font = "Algerian 15")
label_tema.place(x = 80, y = 1)

# Criacao do painel informativo onde será apresentado o resutaldo
label_principal = Label(janela, width=30, height=1, font = "Arial 15 bold", bg = "black", fg = "red", text = "- - - - - - - -")
label_principal.place(x=80, y=55)

label_clima = Label (janela, width=30, height=1, font = "Arial 15 bold", bg = "black", fg = "red", text = "")
label_clima.place(x=80, y=170)

# Criação da Entry onde será introduzido os valores a converter
entry_lista1 = Entry (janela, width=11, bg = "white", fg = "black", font = "Arial 10")
entry_lista1.place(x=220, y=100)

# Criação do combobox inicial do valor de entrada
combo_lista1 = Combobox(janela, width=11, height=1, font="Times 12")
combo_lista1.place(x=120, y=130)
combo_lista1 ["values"] = temperaturas
combo_lista1.current(0)

# Ciaação do Label "para" que indica a diferença das unidades
label_para = Label (janela, text="para", width=5, height=1, bg = "black", fg = "white", font="Arial 12")
label_para.place(x=230, y=130)

# Criação do combobox do valor de conversão de saida 
combo_lista2 = Combobox(janela, width=11, height=1, font="Times 12")
combo_lista2.place(x=280, y=130)
combo_lista2 ["values"] = temperaturas
combo_lista2.current(0)

# Criação do Botão "converter"
botao_3 = Button(janela, width=25, text = "Converter", command=converter)
botao_3.place(x=170, y=230)





janela.mainloop()

