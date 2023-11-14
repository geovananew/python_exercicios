#crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
# ex: apos a sopa ; palindromo: palavra lida de tras pra frente com o mesmo sentido'''

frase = str(input('Digite uma Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'O inveso de {frase} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')