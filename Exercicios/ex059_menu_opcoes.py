'''#Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
o programa deverá realizar a operação solicitada em cada caso'''

n1= int(input('Primeiro valor:'))
n2= int(input('Segundo valor:'))
opcao = 0
while opcao !=5:
    print('''[1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input(">>>> Qual é a sua opção?"))
    if opcao ==1:
        soma = n1 + n2
        print(f'a soma entre {n1} e {n2} é {soma}')
    elif opcao ==2:
        produto= n1* n2
        print(f'O resultado de {n1} x {n2} é {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor:'))
        n1 = int(input('segundo valor:'))
    elif opcao==5:
        print('Opcao inválida. Tente Novamente')
        print('=='*10)
print('Fim do programa!')
