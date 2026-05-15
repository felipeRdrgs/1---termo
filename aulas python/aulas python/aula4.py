# leituras = [50, 40, 30, 20, 10]
# baixos = [50, 55, 52, 30, 20, 15, 10]


# for temp in leituras:
#     if temp > 100:
#         print(f"CRITÍCO: {temp}°C detectado! Acionando parada de emergência.")
#         break 
# for temp1 in baixos:
#     if temp1 < 50:
#         print(f"CRITÍCO: {temp1}°C. detectado! Acionando parada de emergência.")
#         break 
#     else:
#         print(f"temperatura está em {temp1}°C Operação com valores baixos.")
# print("checar sistema. Aguradando manutenção")

# ex 2 
 
# materiais = ["matal", "metal", "plastico", "metal", "vidro", "metal"]
# for peca in materiais:
#     if peca != "metal":
#         print(f"Aviso peça de {peca} detectada. Desviando para descarte...")
#         continue 

#     print(f"Processando peca de {peca}. Furando e polindo...")

# print(f"Fim do lote de produção")

# ativ 1
# tente criar um codigo que conte de 1 a 10, mas use o continue para não imprimir o numero 5

# for numero in range (1,11): 
#     if numero == 5:
#         print(f"ERRO! falha detectada no sensor de numero {numero}.")
#         continue
#     print(f"sensor de numero {numero} funcionando")
# print("contagem finalizada.")

# ativ 2

# from time import sleep 

# for i in range (11):

#     sleep(0.5)
#     print("verde")
# print("siga em frente")

# for i in range (8):

#     sleep(1)
#     print("amarelo")
# print("atenção!")

# for i in range (6):

#     sleep(1)
#     print("vermelho")
# print("aguarde.")

# ativ 3

# maquinas = ['maquina', 'maquina', 'maquina', 'maquina', 'maquina']

# for maquina in maquinas:
#     consumo = (input(f"qual é a quantidade de kwh de cada maquina{maquina}"))
#     print(maquina)
#     totalkwh = consumo + maquina
#     print(f"Total {totalkwh}")

#  ativ 4 

# medidas = [50.1, 49.8, 52.0, 48.5]
# for pecas in medidas:
#     if pecas > 50:
#         print(f"Peças {pecas} Aprovadas.. :)")
#     else: 
#         print(f"Peça {pecas} Rejeitada")

# ativ 5

# sacos = [49.5, 50.0, 51.2, 48.9, 50.5, 47.8]
# for peso in sacos:
#     if 49.0 <= peso <= 51.0:
#         print(f"Saco com peso {peso}kg: Aceitavel")
#     else: 
#         print(f"Saco com peso {peso} kg: Rejeito - fora do limite aceitavel")

# estufa = 0 

# while estufa <5:
#     temp + float(input("digite a temperatura da estufa: "))
#     if temp <0:
#         print("erro de leitura no sensor. Por favor, insira uma temperatura válida.")
#         continue 
#     elif temp > 150: 
#         print("ALERTA CRITICO: risco de explosão!")
#         break
#     else:
#         print(f"Peça {estufa + 1} processada com sucesso a {temp}°C.")
#         estufa += 1 

# ativ 8

for 