# manipulação de aquivos 

# manipulaçao_arquivos = "manupulação de arquivos e textos com python"
# print(manipulaçao_arquivos.upper()) #Maiúsculos 
# print(manipulaçao_arquivos.lower()) #minusculas
# print(manipulaçao_arquivos.strip()) #remove espaços em branco
# print(manipulaçao_arquivos.split()) #DIvide a sring em uma lista de palavras
# print(manipulaçao_arquivos.replace("python", "java")) #troca as palavras
# print(manipulaçao_arquivos.count("a")) # conta quantos vezes a palavra aparece na string
# print(manipulaçao_arquivos.upper().count("python")) # conta quantos vezes a palavra python aparece e deixa em letra maiúscula
# print(manipulaçao_arquivos.find("python")) # retorna a posição da primeira ocorrencia da palavra python 
# print(manipulaçao_arquivos.title()) #converte a primeira letra da palavra para maiúscula
# print(manipulaçao_arquivos.swapcase()) #converte as letras maiúsculas para minusculas
# print(manipulaçao_arquivos.center(50, "*")) # Centraliza a string e preenche com "*" até atingir 50 caracteres
# print(manipulaçao_arquivos.startswith("    Manipulação")) # Verifica se a string começa com "    Manipulação"
# print

# Exercicio 1:
# Crie um algoritmo onde peça para inserir uma frase e deixa-a formatada com maiuscula e acrescente uma contagem de cada frase.

# frase_usuario = input("Inserir frase :) ")
# print(frase_usuario.upper())
# print(frase_usuario.count(frase_usuario))
# print(frase_usuario.count(""))

# Manipulacao de Arquivos
# with open ("sexta.py", "w") as exemplo:
#     exemplo.write("exemplo de clean code - aula 8\n")
#     exemplo.write("continuando a escrever no arquivo\n")
    # write - escreve no arquivo

# Lendo um arquivo

# with open ("arquivo.txt", "w") as exemplo:
#     exemplo.write("Exemplo de Clean Code - Aula 8 \n")
#     exemplo.write("Continuando a escrever no arquivo \n")
# # w = write - Escreve no arquivo, se o arquivo já existir, ele irá sobrescrever o conteúdo.

# with open ("arquivo.py", "w") as python:
#     python.write('print("Exemplo de arquivo Python")')

# with open ("arquivo.py", "r") as python:
#     conteudo = python.read()
#     print(conteudo)
    
# # Lendo um arquivo
# with open ("arquivo.txt", "r") as exemplo:
#     conteudo = exemplo.read()
#     print(conteudo)
# # r = read - Lê o conteúdo do arquivo, se o arquivo não existir, ele irá gerar um erro.

# with open ("arquivo.py","a") as python:
#     python.write('\nprint("Continuando a escrever no arquivo Python")')
#     python.write('\nprint("Mais uma linha no arquivo Python")')
#     python.write('\nprint("Última linha no arquivo Python")')
# a = append - Adiciona conteúdo ao final do arquivo, se o arquivo não existir, ele irá criar um novo arquivo.

#manipulaçao do sistema operacional 
import os 
#criando um diretorio
# os.mkdir("teste")

#renomear pastas
# os.rename("teste","aulas")

# os.mknod("teste.txt")
# os.("aula.txt")

# Listagem de Diretorios
# print(os.listdir()) # Lista os arquivos e pastas do diretório 
# print(os.listdir(".."))
# print(os.listdir("C:\\"))

# exercicio 2 
# Crie um algoritmo para criação de um arquivo que irá desligar o computador.

# with open ("desligar.bat"  ,"w") as desligar:
#     desligar.write("shutdown /s /t 0 /c""sextou! Pode descansar")

# Exercicio 3:
# Crie um algoritmo para cancelar o desligamento do computador.

# with open ("cancelar.bat","w") as cancelar:
#     cancelar.write("shutdown /a /c""desligamento cancelado")

# Exercicio 4:
# Crie um algoritmo para listar os arquivos do diretório atual e do diretório pai.

import os
print(os.listdir())
print(os.listdir(".."))

os.mkdir ("felipin")
os.rename("felipin","picole quent")
os.rmdir("picole quent")




