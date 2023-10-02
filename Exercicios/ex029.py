#escreva um programa que leia a velocidade de um carro
#se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado
#a multa vai custar R$7,00 por cada km acima do limite

velocidade = float(input('informe a veloidade: '))
multa = (velocidade - 80) *7
if velocidade <=80:
    print('Tenha um bom dia, dirija com segurança')
else:
    print(f'você foi multado, a multa custará R${multa:.2f}')