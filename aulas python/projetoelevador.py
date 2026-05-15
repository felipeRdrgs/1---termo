#Sistema de elevador de prédio
# o prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode 
# se mover para cima ou para baixo, e tem a capacidade de tranasportar até 5 pessoas
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa 
# O elevador deve exibir mensagens indicando o andar atula, o número de pessoas no elevador, e as ações realizadas
# O programa deve continuar rodando até que o usuario dedicada encerrar

# levantamento de requisitos:

# requisitos funcionais(RF):
# o elevador deve se mover para cima e para baixo
# o elevador deve ser chamado por qualquer pessoa em qualquer andar
# tem uma capacidade limite de pessoas
# o elevador deve se mover diretamente até o andar em que foi chamado.




# requisitos não funcionais:
# o elevador pode exibir mensagens mostrando o andar atual e o número de pessoas no elevador.
# O programa pode continuar rodando até que o usuario dedicada encerrar.
# o elevador pode começar do andar 0.
# indicar ações realizadas


import time

andar_atual = 0
capacidade = 5
pessoas = int(input("pessoas no elevador"))

while True:

    print("\nELEVADOR AUTOMÁTICO")
    print(f"Andar atual: {andar_atual}")
    print(f"Pessoas no elevador: {pessoas}/{capacidade}")

    input("Pressione ENTER para chamar o elevador...")

    chamada = int(input("Andar de chamada (0 a 10): "))
    destino = int(input("Andar de destino (0 a 10): "))
    entrando = int(input("Quantas pessoas vão entrar? "))

    
    if pessoas + entrando > capacidade:
        print("Elevador lotado!")
        continue

    
    if chamada > andar_atual:

        print("Elevador subindo...")

        for andar in range(andar_atual + 1, chamada + 1):
            time.sleep(1)
            print(f"Andar {andar}")

    elif chamada < andar_atual:

        print("Elevador descendo...")

        for andar in range(andar_atual - 1, chamada - 1, -1):
            time.sleep(1)
            print(f"Andar {andar}")

    andar_atual = chamada

    print(f"Elevador chegou no andar {chamada}")

    
    pessoas += entrando

    print(f"{entrando} pessoa(s) entraram.")
    print(f"Total no elevador: {pessoas}")

    
    if destino > andar_atual:

        print("Elevador subindo...")

        for andar in range(andar_atual + 1, destino + 1):
            time.sleep(1)
            print(f"Andar {andar}")

    elif destino < andar_atual:

        print("Elevador descendo...")

        for andar in range(andar_atual - 1, destino - 1, -1):
            time.sleep(1)
            print(f"Andar {andar}")

    andar_atual = destino

    print(f"Elevador chegou no andar {destino}")

    saindo = int(input("Quantas pessoas vão sair? "))

    if saindo > pessoas:
        saindo = pessoas

    pessoas -= saindo

    print(f"{saindo} pessoa(s) saíram.")
    print(f"Restam {pessoas} pessoa(s) no elevador.")






































