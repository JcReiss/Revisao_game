from operacoes.operaçoes import soma
from funcoes.multiplicar import multiplicar
from funcoes.subtrair import subtrair
from funcoes.verificar_par import verificar_par

#*Desafio 01

"""a = float(input('insira o primeiro valor:'))
b = float(input('insira o segundo valor:'))

print((soma(a,b)))"""



#*Desafio 02
"""
def verificar_inicio (texto):
    if texto.startswith('Olá'):
        print('A sua frase começa com Olá')
    else:
        print('A sua frase não começa com Olá')
   
frase = input("Digite uma frase: ")
verificar_inicio(frase)
"""



#*Questão 03
"""
criar_arquivo = []
with open('nome_arquivo.txt', 'w') as arquivo:
    arquivo.write('Hello World!\n')
"""



#*Questão 04
"""valores = []
soma = 0
with open('valores.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        try:
            numero = float(linha)
            if numero % 3 == 0:
                valores.append(numero)
        except ValueError:
            print(f"Valor invalido e encontrado e removido: {linha}")
print(f"A soma dos números é :{valores}")

for valor in valores:
    soma += valor
print(f'{soma}')"""


#*Questão 05
"""
a = float(input(f'digite o primeiro número da multiplicação:'))
b = float(input(f'digite o segundo número da multiplicação:'))

print(f'O resultado da multiplicação é: {multiplicar (a,b)}')
"""



"""
a = float(input(f'Digite o primerio valor da subtração:'))
b = float(input(f'Digite o segundo valor da subtração:')) 

print(f'o resultado da subtração é: {subtrair (a,b)}')
"""



"""
numero = int(input("Insira um número para a verificar se ele é par: "))
if verificar_par(numero):
    print(f"O número {numero} é par!")
else:
    print(f"O número {numero} não é par!")
"""


#*Questão 08
"""
with open('palavras.txt', 'r', encoding='utf-8') as arquivo:
    palavras = arquivo.read().split() 


palavras_filtradas = []
for palavra in palavras:
    if palavra.lower().startswith('b') and palavra.lower().endswith('o'):
        palavras_filtradas.append(palavra)

with open('palavras_filtradas.txt', 'w', encoding='utf-8') as arquivo:
    for palavra in palavras_filtradas:
        arquivo.write(palavra + '\n') 

print("As palavras foram filtradas e salvas em 'palavras_filtradas.txt'.")
"""