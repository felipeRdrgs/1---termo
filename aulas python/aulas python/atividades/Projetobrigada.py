# 1. Cadastro de Funcionários:
# ○ Armazene o nome, setor e o status dos treinamentos (NR-10, NR-35 e
# Brigada).

# 2. Verificação de EPI (NR-6):
# ○ O sistema deve receber o setor do funcionário.
# ○ Se o setor for "Elétrica", liste a obrigatoriedade de luvas de alta tensão e
# botas dielétricas.
# ○ Se o setor for "Trabalho em Altura", liste o cinturão de segurança e
# talabarte.
# 3. Alerta de Reciclagem:
# ○ Crie uma função que receba o ano do último treinamento da Brigada de
# Incêndio.
# ○ Se o treinamento tiver mais de 2 anos, exiba a mensagem: "Treinamento
# Vencido! Encaminhar para reciclagem."
# ○ Caso contrário, exiba: "Treinamento Válido."


# Requisitos Funcionais (RF):
# .O sistema deve armazenar o nome, setor e status de treinamento de cada funcionario.
# .Se o setor for da eletrica, listar a obrigatoriedade de equipamentos como botas dielétricas e luvas de alta tensão 
# .Se o setor for de Trabalho em Altura, liste o cinturão de segurança e talabarte.
# Exiba na tela um resumo com o total de funcionários cadastrados e quantos estão com treinamentos em dia.

# Requisitos Funcionais (RF):
# O sistema deve receber o setor do funcionário.
# Crie uma função que receba o ano do último treinamento da Brigada de incêndio
# Se o treinamento tiver mais de 2 anos, exiba a mensagem: "Treinamento Vencido! Encaminhar para reciclagem."

def identificação_de_funcionario():
    print("Projeto Brigada: Sistema de Gestão de Segurança do Trabalho (SESMT)")
    nome_funcionario = input("Qual é o seu nome? ")
    setor_funcionario = input("Qual é o seu setor? \n1- elétrica \n2- trabalho em altura\n")

    if setor_funcionario == "1":
        print("Verificação de EPI.")
        print("Itens obrigatórios a serem utilizados neste setor:\n1- luvas de alta tensão\n2- botas dielétricas")
    elif setor_funcionario == "2":
        print("Verificação de EPI.")
        print("Itens obrigatórios a serem utilizados neste setor:\n1- cinturão de segurança\n2- talabarte")
    else:
        print("Setor não reconhecido. Informe 1 ou 2.")

    resposta_epi = input("Você possui os itens listados acima? \n1- S \n2- N\n")
    if resposta_epi == "s":
        print("Exigências cumpridas.")
    elif resposta_epi == "n":
        print("Você não possui os itens obrigatórios. Certifique-se de possuí-los.")
    else:
        print("Resposta inválida.")

    return nome_funcionario, setor_funcionario

while True:
    nome, setor = identificação_de_funcionario()
    print(f"Bem-vindo funcionário. Você está sendo identificado como {nome}, setor {setor}.")
    break

ano_treinamento = float(input("digite o ano do último treinamento da brigada de incendio:"))

if ano_treinamento > 2:
    print("treinamento vencido! encaminhar para reciclagem.")
else:
    print("treinamento válido.")

total_funcionarios = 1
funcionarios_treinados = 1 
print(f"Total de funcionários cadastrados: {total_funcionarios} \nFuncionários com treinamentos em dia: {funcionarios_treinados}")












