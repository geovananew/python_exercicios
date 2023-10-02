#Faça um programa que leia a largura e altura de uma parede em metros,
# calcule a sua área e quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m²

largura= float(input('largura da parede: '))
altura = float(input('altura da parede: '))
area = largura * altura
print(f'sua parede tem a dimensão de {largura} x {altura} e sua área é de {area}')
tinta = area/2
print(f'para pintar essaparede você precisará de {tinta}l de tinta' )
