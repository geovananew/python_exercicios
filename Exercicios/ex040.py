#crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# média abaixo de 5.0: reprovado;
# média entre 5.0 e 6.9: recuperação;
# média 7.0 ou superior: aprovado

nota1 = float(input('informe sua primeira nota: '))
nota2 = float(input('informe sua segunda nota: '))
media = (nota1+nota2)/2
print(f'tirando {nota1} e {nota2} a média é igual a {media}')
if  media <5:
    print('nota abaixo da média, REPROVADO!')
elif media <=5 and media <7:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')