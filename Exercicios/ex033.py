#Faça um programa que leia três números emostre qual é o maior e qual é o menor
''''
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificando quem é o menor
menor = a
if b<a and b<c:
    menor= b
if c<a and c<b:
    menor = c
#Verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'o menor valor é {menor}')
print(f'o maior valor é {maior} ')
'''


p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
t = int(input('Terceiro valor: '))
maximo = max(p, s, t)
minimo = min(p, s, t)

print(f'O menor valor digitado foi {minimo}')
print(f'O maior valor digitado foi {maximo}')
