#Faça um programa que leia uma frase pelo teclado e mostre:
# --> quantas vezes aparece a letra 'a'
# --> em que posição ela aparece a primeira vez
# --> em que posição ela aparece a última vez

from Scripts.bottle import unicode

frase = str(input('Digite uma frase: ')).upper().strip()
print(f'a letra "A" aparece {frase.count("A")} vezes')
print(f'a primeira letra "A" apareceu na posição {frase.find("A")+1}')
print(f'a última letra "A" apareceu na posição {frase.rfind("A")+1}') #r.find significa para começar a procurar a partir do lado direito