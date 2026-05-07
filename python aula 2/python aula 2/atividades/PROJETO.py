# ● O estacionamento possui um total de 500 vagas.
# ● O sistema deve manter um contador de vagas ocupadas. Se o estacionamento estiver lotado, a
# cancela de entrada não deve abrir para novos clientes (exceto para quem possui Tag de Acesso
# Rápido, pois estes têm vagas reservadas

import time

numero_vagas = 500
vagas_ocupadas = 0

while True:
    print("bem-vindo ao shopping pátio.")
    horario = float(input("informe o horário de entrada."))
    tipo_acesso = int(input("qual é seu tipo de acesso? \n 1- ticket \n 2- tag \n"))
    if tipo_acesso == 2:
        print("Acesso via TAG liberado. Seja bem vindo! - ", horario,)
    elif tipo_acesso == 1:
        if vagas_ocupadas < numero_vagas:
            print("precione o botão a baixo.")
        time.sleep(2)
        print("verificando vagas disponíveis...")
        time.sleep(4)
        print("vaga encontrada! pegue seu ticket e siga em frente. -", horario,)
        vagas_ocupadas += 1
        break
    else:
        print("Estacionamnto lotado. aguarde.")
    if tipo_acesso == 2:
        print("Siga em frente.")
        vagas_ocupadas += 1
        print("vagas ocupadas:", vagas_ocupadas)
        break

import time 

valor = 0

print("Saída do estacionamento.")

ticket = input("você possui o ticket de entrada? \n 1-sim \n 2-não \n")
if ticket == "2":
    print("saída sem ticket.")
    print("taxa: R$ 50,00")
    valor = 50
else:
    tempo = float(input("quantas horas você utilizou o estacionamnto?"))
    if tempo <= 0.25:
        valor = 0
        print("tempo de toleância. Gratuito.")
    elif tempo <= 3:
        valor = 15
        print("valor fixo de R$ 15.00.")
    else:
        horas_extras = int(tempo -3)
        if tempo - 3 > horas_extras:
            horas_extras += 1
        print("Cobrança por horas extras aplicada.")
    tag = input("você possui TAG? \n 1-sim \n 2-não \n")
    if tag == "1":
        valor = valor * 0.9
        print("Desconto de 10% para TAG aplicado.")
    print("Valor total a pagar: R$", valor,".")
    pago = input("Pagamento realizado? \n 1-sim \n 2-não \n")
    if pago == "1":
        print("Pagamento confirmado. Cancela liberada.")
    else:
        print("Pagamento pendente. Saída bloqueada.")

        










