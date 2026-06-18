# ● O estacionamento possui um total de 500 vagas.
# ● O sistema deve manter um contador de vagas ocupadas. Se o estacionamento estiver lotado, a
# cancela de entrada não deve abrir para novos clientes (exceto para quem possui Tag de Acesso
# Rápido, pois estes têm vagas reservadas

import time

numero_vagas = 500
vagas_ocupadas = 0
multa_ticket = 50

print("Bem-vindo ao shopping")


horario = float(input("Informe o horário de entrada: "))
tipo_acesso = int(input("Qual é seu tipo de acesso?\n1 - Ticket\n2 - TAG\n"))


if vagas_ocupadas >= numero_vagas:
    print("Estacionamento lotado. Aguarde.")
else:

    
    if tipo_acesso == 2:
        print("Acesso via TAG liberado.")
        print("Horário de entrada:", horario)
        print("Siga em frente.")

    
    elif tipo_acesso == 1:
        input("Pressione o botão a baixo para retirar o ticket.")
        print("Verificando vagas disponíveis...")
        time.sleep(2)

        print("Vaga encontrada!")
        print("Pegue seu ticket e siga em frente.")
        print("Horário de entrada:", horario)

    else:
        print("Tipo de acesso inválido.")

vagas_ocupadas += 1
print("Vagas ocupadas:", vagas_ocupadas)

print(" Saída do estacionamento")

tempo = float(input("\nQuantas horas você utilizou o estacionamento? "))

total_pagamento = 0

    
if tempo <= 0.15:
    total_pagamento = 0
    print("Tempo de tolerância. Gratuito.")

elif tempo <= 3:
        total_pagamento = 15
        print("Valor fixo de R$15.00.")

else:
    horas_extras = tempo - 3

        
if horas_extras != int(horas_extras):
            horas_extras = int(horas_extras) + 1
else:
            horas_extras = int(horas_extras)

total_pagamento = 15 + (horas_extras * 5)

print("Cobrança por horas extras aplicada.")
print("Horas extras:", horas_extras)

    
tag = input("\nVocê possui TAG?\n1 - Sim\n2 - Não\n")

if tag == "1":
        desconto = total_pagamento * 0.10
        total_pagamento -= desconto
        print("Desconto de 10% aplicado.")

else:
        print("Desconto não aplicado.")

    
ticket = input("\nVocê ainda possui o ticket?\n1 - Sim\n2 - Não\n")

if ticket == "2":
        total_pagamento += multa_ticket
        print("Multa de R$50,00 aplicada.")

else:
        print("Tudo certo com o ticket.")

    
print(f"\nValor total a pagar: R$ {total_pagamento:.2f}")

    
pagamento = int(input("\nQual será a forma de pagamento?\n""1 - Crédito\n""2 - Débito\n""3 - PIX\n"))

if pagamento in [1, 2, 3]:
        print("Processando pagamento...")
        time.sleep(2)

        print("Pagamento realizado com sucesso!")
        print("Tenha um bom dia!")

else:
        print("Forma de pagamento inválida.")




        










