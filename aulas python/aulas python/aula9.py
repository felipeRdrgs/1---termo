    # 1. O PROBLEMA DA IDADE
idade = input("digite sua idade:")
if idade >=18:
    print("você é maior de idade.")

    # corrigido:
idade = float(input("digite sua idade:"))
if idade >=18:
    print("você é maior de idade.")
elif idade <=18:
    print("você é menor de idade")

    # 2. A ESCRITA FIEL
nome = "Mariana"
print("Seja bem-vinda, nome!")

    # corrigido:
nome = "mariana"
print("Seja bem vinda", nome )

    # 3. FALTA DE ESPAÇO
numero = 10
if numero > 5:
print("O número é maior que cinco.")
else:
print("O número é menor ou igual a cinco.")

    # corrigido:
numero = float(input("qual é o número?"))
if numero > 5:
    print("o número é maior que cinco.")
else: 
    print("o número é menor ou igual a cinco.")

    # 4. ESQUECIMENTO FATAL
usuario = "aluno123"
if usuario == "aluno123"
print("Login realizado com sucesso.")

    # corrigido:
usuario = input("digite seu nome de usuario.")
if usuario == "aluno123":
    print("login realizado com sucesso.")
else:
    print("não foi possivel realizar o login.")

    # 5. ATRIBUIÇÃO VS. COMPARAÇÃO
clima = "ensolarado"
if clima = "chuvoso":
print("Leve um guarda-chuva!")

    # corrigido:
clima = input("qual é o estado atual do clima?")
if clima == "chuvoso":
    print("leve um guarda chuva!")
elif clima == "ensolarado":
    print("pode ir tranquilo, dia ensolarado.")

    # 6. MISTURANDO ALHOS COM BUGALHOS
pontos = 50
print("Parabéns! Você fez " + pontos + " pontos.")
    
    #  corrigido:
pontos = "+50 pontos"
print("parabéns! Você fez", pontos)

    # 7. A OORDEM DOS FATORES
nota = 9.5
if nota >= 7:
print("Aprovado")
elif nota >= 9:
print("Excelente!")

    # corrigido:
nota = float(input("qual foi sua nota?"))
if nota == 7:
    print("aprovado.")
elif nota == 8:
    print("aprovado.")
elif nota >=9:
    print("excelente!")
elif nota <7:
    print("não aprovado")

    # 8. O CONTADOR DE 1 A 5
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
for i in range(5):
print(i)

    # corrigido:
for i in range(1 ,6):
    print(i)

    # 9. O LOOP ETERNO
tentativas = 1
while tentativas <= 3:
print("Tentando conectar...")


    # corrigido:
tentativas = 1 
while tentativas <= 3:
    print("tentando  conectar...")
    tentativas = tentativas +1

    # 10. A SENHA TEIMOSA
# O programa deve pedir a senha até que o usuário digite "python123"
senha = ""
while senha == "python123":
senha = input("Digite a senha secreta: ")
print("Acesso concedido!")

    # corrigido
senha = ""
while senha != "python123":
    senha = input("digite a senha secreta:")
print("acesso concedido!")





