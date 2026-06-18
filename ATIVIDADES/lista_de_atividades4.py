import tkinter as tk
from tkinter import messagebox

def calcular_idade():
    nome = campo_nome.get()
    nascimento = int(campo_nascimento.get())

    if nascimento == "":
        messagebox.showerror("Erro", "Por favor, insira um ano de nascimento válido.")
        return
    else:
        ano_atual = 2026
        idade = ano_atual - int(campo_nascimento.get())
    messagebox.showinfo("Resultado", f"{nome}, sua idade é: {idade} anos.")
    


janela = tk.Tk()
janela.title("calculando idade")
janela.geometry("500x500")

lbl_nome = tk.Label(janela, text="informe seu nome a baixo:")
lbl_nome.pack(pady=1)

campo_nome = tk.Entry(janela, font=("arial", 12))
campo_nome.pack(pady=15)

lbl_nascimento = tk.Label(janela, text="informe o ano que você nasceu:")
lbl_nascimento.pack(pady=10)

campo_nascimento = tk.Entry(janela, font=("arial", 12))
campo_nascimento.pack(pady=10)

btn_calcular = tk.Button(janela, text="cadastrar", command=calcular_idade)
btn_calcular.pack(pady=5)

btn_fechar = tk.Button(janela, text="fechar", command=janela.destroy)
btn_fechar.pack(pady=5)




janela.mainloop()