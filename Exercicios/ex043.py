#desenvolva uma lógica que leia o peso e altura de uma pessoa,
# calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
#abaixo de 18.5: abaixo do peso;
# entre 18.5 e 25:peso ideal;
# 25 até 30:sobrepeso;
# 30 até 40: obesidade;
# acima de 40: obesidade mórbida

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('E a sua altura? '))
imc = peso / (altura * altura)
if imc <=18.5:
    print(f'o IMC é {imc}, está abaixo do peso')
elif imc <=25:
    print(f'o IMC é {imc}, está no peso ideal')
elif imc <=30:
    print(f'o IMC é {imc}, está com sobrepeso')
elif imc <=40:
    print(f'o IMC é {imc}, está com obesidade')
else:
    print(f'o IMC é {imc}, está com obesidade morbida')