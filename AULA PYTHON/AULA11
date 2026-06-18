# tkinter 

# componentes pricipais
# tk : janela
# label: texto em rotulo 
# button: um botão de clique
# entry: um campo de entrada de texto

# # blibioteca
# import tkinter as tk 
# from tkinter import messagebox

# # 1. criar janela 
# janela = tk.Tk()
# janela.configure(bg="gray")
# janela.title("minha primeira janela em GUI")
# janela.geometry("400x200") #largura e altura

# # showinfo: mensagem de informação informação
# # showerror: mensagem de erro 
# # showarning: mensagem de aviso

# # 2. criar a função que o botão vai execultar
# def mostrar_mensagem():
#     messagebox.showinfo("sucesso, você clicou no botão! 🙃")

# # 3. criar componentes
# lbl_titulo = tk.Label(janela, text="bem-vindo a aula de tkinter!",
# font=("Arial", 14, "bold"), bg="gray")
# btn_clique = tk.Button(janela, text="clique aqui 🙃 ", font=("arial", 14), bg="#8bd2a9", fg="white", command=mostrar_mensagem)


# # 4. posicionar componentes 

# lbl_titulo.pack(pady=20)
# btn_clique.pack(padx=20)
# #pady - posicionar margem vertical
# #padx - posicionar horizontal

# # 5. rodar o loop da interface
# janela.mainloop()

import tkinter as tk
from tkinter import messagebox

# 1. configurar evento

def solicitar_informações():
    # .get() serve para buscar o texto que foi digitado 
    nome_usuario = campo_nome.get()

    if nome_usuario == "":
        messagebox.showwarning("aviso", "por favor, digite seu nome")

    else:
        messagebox.showinfo("saudações, querido aluno", f"olá, {nome_usuario} seja bem-vindo ao undo das interfaces graficas.")

# 2.configuração de janela
app = tk.Tk()
app.title("tela de usuario")
app.geometry("300x300")
app.configure(bg="blue")

# 3. componentes
lbl_nome_usuario = tk.Label(app, text="digite seu nome")
lbl_nome_usuario.pack(pady=10)

campo_nome = tk.Entry(app, font=("arial", 12))
campo_nome.pack(pady=5)

lbl_idade_usuario = tk.Label(app, text="informe sua idade")
lbl_idade_usuario.pack(pady=20)

campo_idade = tk.Entry(app, font=("Helvetica", 12))
campo_idade.pack(pady=5)

btn_cadastrar = tk.Button(app, text="cadastrar", command=solicitar_informações)
btn_cadastrar.pack(pady=5)

btn_fechar = tk.Button(app, text="Fechar", command=app.destroy)
btn_fechar.pack(pady=10)


# 4. rodar interface
app.mainloop()




















