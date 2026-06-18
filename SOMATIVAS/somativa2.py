# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# import tkinter as tk
# from tkinter import messagebox
# def registrar_operador():
#     nome_operador = campo_nome.get()
#     turno_operador = campo_turno.get().upper()

#     if nome_operador == "" or turno_operador not in ["A", "B", "C"]:
#         messagebox.showerror("Erro", "Por favor, digite um nome válido e um turno (A, B ou C).")
#     else:
#         messagebox.showinfo("Registro Completo", f"Operador {nome_operador} registrado no Turno {turno_operador}. Boa jornada!")
# janela = tk.Tk()
# janela.title("Registro de Operador")
# janela.geometry("400x250")

# lbl_nome = tk.Label(janela, text="Digite o nome do operador:", font=("Arial", 12))
# lbl_nome.grid(row=0, column=0, padx=10, pady=10)

# campo_nome = tk.Entry(janela, font=("Arial", 12))
# campo_nome.grid(row=1, column=0, padx=10, pady=10)

# lbl_turno = tk.Label(janela, text="Digite o turno (A, B ou C):", font=("Arial", 12))
# lbl_turno.grid(row=2, column=0, padx=10, pady=10)

# campo_turno = tk.Entry(janela, font=("Arial", 12))
# campo_turno.grid(row=3, column=0, padx=10, pady=10)

# btn_registrar = tk.Button(janela, text="Registrar", font=("Arial", 12), command=registrar_operador)
# btn_registrar.grid(row=4, column=0, padx=10, pady=10)

# btn_fechar = tk.Button(janela, text="Fechar Janela", font=("Arial", 12), command=janela.destroy)
# btn_fechar.grid(row=5, column=0, padx=10, pady=10)


# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

# import tkinter as tk
# from tkinter import messagebox

# def calculo():
#     if:
#         pecas = int(campo_quantidade.get())
#         horas = float(campo_horas.get())

#         producao = pecas / horas

#         messagebox.showinfo(
#             "Resultado",
#             f"Foram produzidas {pecas} peças em {horas} horas.\n"
#             f"Produção por hora: {producao:.2f} peças/h"
#         )

#     else :
#         messagebox.showerror("Erro", "Digite apenas números!")

# janela = tk.Tk()
# janela.title("Cálculo de Produção")
# janela.geometry("400x250")

# lbl_horas = tk.Label(janela, text="Informe a quantidade de horas:", font=("Arial", 12))
# lbl_horas.grid(row=0, column=0, padx=10, pady=10)

# campo_horas = tk.Entry(janela, font=("Arial", 12))
# campo_horas.grid(row=1, column=0, padx=10, pady=10)

# lbl_quantidade = tk.Label(janela, text="Informe a quantidade de peças produzidas:", font=("Arial", 12))
# lbl_quantidade.grid(row=2, column=0, padx=10, pady=10)

# campo_quantidade = tk.Entry(janela, font=("Arial", 12))
# campo_quantidade.grid(row=3, column=0, padx=10, pady=10)

# btn_dados = tk.Button(janela, text="Concluir", font=("Arial", 12), command=calculo)
# btn_dados.grid(row=4, column=0, padx=10, pady=10)

# btn_fechar = tk.Button(janela, text="Fechar Janela", font=("Arial", 12), command=janela.destroy)
# btn_fechar.grid(row=5, column=0, padx=10, pady=10)

# janela.mainloop()

# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.


# import tkinter as tk
# from tkinter import messagebox
# def converter():
#     if campo_bar.get() == "":
#         messagebox.showerror("Erro", "Por favor, digite um valor em Bar.")
#         return

#     try:
#         bar = float(campo_bar.get())
#         psi = bar * 14.5
#         messagebox.showinfo("Resultado", f"{bar:.2f} Bar é equivalente a {psi:.2f} PSI.")
#     except ValueError:
#         messagebox.showerror("Erro", "Digite um número válido para Bar.")

# janela = tk.Tk()
# janela.title("Conversor de Unidade")
# janela.geometry("400x250")

# lbl_bar = tk.Label(janela, text="Digite a pressão em Bar:", font=("Arial", 12))
# lbl_bar.grid(row=0, column=0, padx=10, pady=10)

# campo_bar = tk.Entry(janela, font=("Arial", 12))
# campo_bar.grid(row=1, column=0, padx=10, pady=10)

# btn_converter = tk.Button(janela, text="Converter", font=("Arial", 12), command=converter)
# btn_converter.grid(row=2, column=0, padx=10, pady=10)

# btn_fechar = tk.Button(janela, text="Fechar Janela", font=("Arial", 12), command=janela.destroy)
# btn_fechar.grid(row=3, column=0, padx=10, pady=10)

# janela.mainloop()

# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.

# import tkinter as tk
# from tkinter import messagebox

# def calcular_media():
#     if campo_nota1.get() == "" or campo_nota2.get() == "" or campo_nota3.get() == "":
#         messagebox.showerror("Erro", "Por favor, preencha todas as notas.")
#         return

# lbl_nota1 = tk.Label(janela, text="Digite a primeira nota (0-10):", font=("Arial", 12))
# lbl_nota1.grid(row=0, column=0, padx=10, pady=10)

# campo_nota1 = tk.Entry(janela, font=("Arial", 12))
# campo_nota1.grid(row=1, column=0, padx=10, pady=10)

# lbl_nota2 = tk.Label(janela, text="Digite a segunda nota (0-10):", font=("Arial", 12))
# lbl_nota2.grid(row=2, column=0, padx=10, pady=10)

# campo_nota2 = tk.Entry(janela, font=("Arial", 12))
# campo_nota2.grid(row=3, column=0, padx=10, pady=10)

# lbl_nota3 = tk.Label(janela, text="Digite a terceira nota (0-10):", font=("Arial", 12))
# lbl_nota3.grid(row=4, column=0, padx=10, pady=10)

# campo_nota3 = tk.Entry(janela, font=("Arial", 12))
# campo_nota3.grid(row=5, column=0, padx=10, pady=10)

# btn_calcular = tk.Button(janela, text="Calcular Média", font=("Arial", 12), command=calcular_media)
# btn_calcular.grid(row=6, column=0, padx=10, pady=10)

# btn_fechar = tk.Button(janela, text="Fechar Janela", font=("Arial", 12), command=janela.destroy)
# btn_fechar.grid(row=7, column=0, padx=10, pady=10)
# janela.mainloop()

# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# import tkinter as tk
# from tkinter import messagebox

# def calcular_temperatura():
#     temperatura_motor = float(ent_temperatura_motor.get())

#     if temperatura_motor < 40:
#         messagebox.showinfo("Temperatura do Motor", "Baixa carga")
#     elif temperatura_motor >= 40 and temperatura_motor <= 70:
#         messagebox.showinfo("Temperatura do Motor", "Normal")
#     elif temperatura_motor > 70:
#         messagebox.showinfo("Temperatura do Motor", "ALERTA: Resfriamento Ativado!")

# janela = tk.Tk()
# janela.title = ("Termostato Inteligente")
# janela.geometry("500x500")

# lbl_temperatura_motor = tk.Label(janela, text="Insira a temperatura atual do motor abaixo:", font=("Arial", 14))
# lbl_temperatura_motor.grid(row=1, column=1, pady=10, padx=10)

# ent_temperatura_motor = tk.Entry(janela, font=("Arial", 14))
# ent_temperatura_motor.grid(row=2, column=1, pady=10, padx=10)

# btn_temperatura_motor = tk.Button(janela, text="Calcular temperatura", width=19, height=1, command=calcular_temperatura)
# btn_temperatura_motor.grid(row=3, column=1, pady=10, padx=10)

# janela.mainloop()


# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("Classificador de Lotes")
# janela.geometry("400x250")

# lbl_codigo = tk.Label(janela, text="Digite o código do produto:", font=("Arial", 12))
# lbl_codigo.grid(row=0, column=0, padx=10, pady=10)
# campo_codigo = tk.Entry(janela, font=("Arial", 12))
# campo_codigo.grid(row=1, column=0, padx=10, pady=10)
# def classificar_lote():
#     codigo = campo_codigo.get().upper()

#     if codigo.startswith("A"):
#         messagebox.showinfo("Classificação", "Alimentos")
#     elif codigo.startswith("E"):
#         messagebox.showinfo("Classificação", "Eletrônicos")
#     else:
#         messagebox.showinfo("Classificação", "Desconecido")
# btn_classificar = tk.Button(janela, text="Classificar", font=("Arial", 12), command=classificar_lote)
# btn_classificar.grid(row=2, column=0, padx=10, pady=10)

# btn_fechar = tk.Button(janela, text="Fechar Janela", font=("Arial", 12), command=janela.destroy)
# btn_fechar.grid(row=3, column=0, padx=10, pady=10)
# janela.mainloop()

# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.

# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("Segurança de Operação")
# janela.geometry("400x250")

# lbl_sensor = tk.Label(janela, text="Estado do sensor da porta (fechada/aberta):", font=("Arial", 12))
# lbl_sensor.grid(row=0, column=0, padx=10, pady=10)

# campo_sensor = tk.Entry(janela, font=("Arial", 12))
# campo_sensor.grid(row=1, column=0, padx=10, pady=10)
# lbl_botao = tk.Label(janela, text="Estado do botão de emergência (ligado/desligado):", font=("Arial", 12))
# lbl_botao.grid(row=2, column=0, padx=10, pady=10)

# campo_botao = tk.Entry(janela, font=("Arial", 12))
# campo_botao.grid(row=3, column=0, padx=10, pady=10)

# def verificar_seguranca():

#     sensor_porta = campo_sensor.get().lower()
#     botao_emergencia = campo_botao.get().lower()

#     if sensor_porta == "fechada" and botao_emergencia == "desligado":
#         messagebox.showinfo("Segurança", "A máquina pode iniciar.")
#     else:
#         messagebox.showwarning("Segurança", "A máquina NÃO pode iniciar. Verifique os estados do sensor e do botão de emergência.")

# btn_verificar = tk.Button(janela, text="Verificar Segurança", font=("Arial", 12), command=verificar_seguranca)
# btn_verificar.grid(row=4, column=0, padx=10, pady=10)
# janela.mainloop()

# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

# import tkinter as tk
# from tkinter import messagebox

# def calcular_descarte():
#     total_pecas = float(campo_total.get())
#     pecas_defeituosas = float(campo_defeituosas.get())

#     percentual_descarte = (pecas_defeituosas / total_pecas) * 100

#     if percentual_descarte > 5:
#         messagebox.showinfo("Resultado", "Revisar Processo")
#     else:
#         messagebox.showinfo("Resultado", "Processo Otimizado")
    

# janela = tk.Tk()
# janela.title("Cálculo de Descarte")
# janela.geometry("500x300")

# lbl_total = tk.Label(janela, text="Total de peças produzidas:", font=("Arial", 12))
# lbl_total.grid(row=0, column=0, padx=10, pady=10)

# campo_total = tk.Entry(janela, font=("Arial", 12))
# campo_total.grid(row=1, column=0, padx=10, pady=10)

# lbl_defeituosas = tk.Label(janela, text="Total de peças defeituosas:", font=("Arial", 12))
# lbl_defeituosas.grid(row=2, column=0, padx=10, pady=10)

# campo_defeituosas = tk.Entry(janela, font=("Arial", 12))
# campo_defeituosas.grid(row=3, column=0, padx=10, pady=10)

# btn_calcular = tk.Button(janela, text="Calcular Descarte", font=("Arial", 12), command=calcular_descarte)
# btn_calcular.grid(row=4, column=0, padx=10, pady=10)

# btn_fechar = tk.Button(janela, text="Fechar Janela", font=("Arial", 12), command=janela.destroy)
# btn_fechar.grid(row=5, column=0, padx=10, pady=10)

# janela.mainloop()

# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.

# import tkinter as tk
# from tkinter import messagebox 

# def validaçao():
#     medida = float(campo_medida.get())

#     if medida < 9.8:
#         messagebox.showinfo("Resultado", "A peça está abaixo da tolerância.")
#     elif medida > 10.2:
#         messagebox.showinfo("Resultado", "A peça está acima da tolerância.")
#     else:
#         messagebox.showinfo("Resultado", "A peça está dentro da tolerância.")

# janela = tk.Tk()
# janela.title("validação de medida")
# janela.geometry("400x200")

# lbl_medida = tk.Label(janela, text="qual é a medida da peça?", font=("arial", 12))
# lbl_medida.grid(row=0, column=0, padx=10, pady=10)

# campo_medida = tk.Entry(janela, font=("arial", 12))
# campo_medida.grid(row=1, column=0, padx=10, pady=10)

# btn_verificar =tk.Button(janela,text="verificar", font=("Arial",14),width=7,height=1, command=validaçao)
# btn_verificar.grid (row=2,column=0,padx=20,pady=20)

# btn_fechar =tk.Button(janela,text=" Fechar ",font=("Arial",14),width=7,height=1,command=janela.destroy)
# btn_fechar.grid (row=2, column=1,padx=20,pady=20)

# janela.mainloop()

# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

# import tkinter as tk
# from tkinter import messagebox

# def contagem_regressiva():
#     for i in range(10, 0, -1):
#         messagebox.showinfo("Contagem Regressiva", f"Contagem: {i}")
#     messagebox.showinfo("Contagem Regressiva", "Prensa Ativada!")
    
# janela = tk.Tk()
# janela.title("Contagem Regressiva de Setup")
# janela.geometry("400x250")

# btn_iniciar = tk.Button(janela, text="Iniciar Contagem Regressiva", font=("Arial", 12), command=contagem_regressiva)
# btn_iniciar.pack(pady=20)

# btn_fechar = tk.Button(janela, text="Fechar Janela", font=("Arial", 12), command=janela.destroy)
# btn_fechar.pack(pady=10)
# janela.mainloop()


