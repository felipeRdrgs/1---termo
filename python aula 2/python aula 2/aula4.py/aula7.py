# # aula 7

# print("registro de veículo")
# modelo_veiculo = input("qual é o modelo do veículo")
# placa_veiculo = input("qual é a placa do veículo")
# print(f"veículo {modelo_veiculo} de placa {placa_veiculo} registrado no sistema. Boa viagem!")

# print("calculo de autonomia")
# capacidade_tanque = float(input("digite a capacidade de litros"))
# consumo_medio = float(input("digite o consumo do caminhão em km/1"))
# total = capacidade_tanque * consumo_medio
# print(f"capacidade {capacidade_tanque} do tanque e sua distancia {consumo_medio} em média KM/L e o total {total}")

# print("conversor de moeda (frete internacional)")
# valorfrete = float(input("valor de frete em dolar"))
# conversaoreal = float(input("valor da taxa em reais"))
# totalconversao = valorfrete * conversaoreal
# print(f"o valor do frete foi {valorfrete} e a taxa aplicada foi de {conversaoreal} e o total do frete {totalconversao:.2f}")
# print("o valor do frete foi", valorfrete,"e a taxa aplicada foi de", conversaoreal,"e o total do frete", round(totalconversao,2))

# print("media de entregas")
# rota1 = int(input("digite a primeira rota em horas"))
# rota2 = int(input("digite a segunda rota em horas"))
# rota3 = int(input("digite a terceira rota em horas"))
# mediarota = (rota1 + rota2 + rota3) /3
# print(f"a media de entregas das 3 rotas realizadas foi de... {mediarota:.2f}")

# print("monitor de carga")
# pesocaminhao = float(input("informe o peso do caminhão em toneladas"))
# if pesocaminhao <= 10:
#     print("a carga esta leve ☺️")
# elif pesocaminhao < 25:
#     print("carga padrão.")
# elif pesocaminhao >= 25:
#     print("ALERTA: excesso de peso!")
# else:
#     print("digite outro valor")

# print("classificador de destino - código de cargas")
# print("código de cargas = N - norte S - Sul e Outros internacionais")
# codigocarga = input("inserir código da carga").upper()
# if codigocarga == "N":
#     print("regiao norte")
# elif codigocarga ==  "S":
#     print("região sul")
# elif codigocarga == "0":
#     print("região internacional")
# else:
#     print("regiao internacional")


print("liberação de saida - checklist e motorista")
checklist = input("o checklist foi realizado (concluido ou não concluido)")
motorista = input("0 motorista foi identificado (sim ou não)")

if checklist == "concluido" and motorista == "sim":
    print("iniciar rota - boa viagem")
else:
    print("voltar e realizar o checklist 😭")

# print("calculo de atrasos")
# entregas = int(input("quantidade de entregas agendadas"))
# entregasatraso = int(input("quantidade de entregas com atraso"))
# total = entregasatraso / entregas 
# if total > 0.1:
#     print("necessario otimizar rotas")
# else:
#     print("logistica eficiente")

# print("validação de calibragem")
# cargapressao = float(input('digite e media da pressão em PSI dos pneus'))
# if cargapressao >=110:
#     print("acima do recomendado")
# else:
#     print("dentro do padrão recomendado")
# print("contagem de embarque")
# for embarque in range(5,0,-1):
#     time.sleep(1)
#     print(f"embarque em: {embarque}")
































































