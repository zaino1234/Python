print('-'*40)
print(f'{"Calculadora do Valor da Tinta":^40}')
print('-'*40)
# cada litro de tinta pinta uma área de 2 metros quadrado
largura = float(input('Largura da Parede: m '))
altura = float(input('Altura da Parede: m '))
area = largura*altura
print(f'Sua parede tem a dimensão de {largura}m x {altura}m e '
      f'sua área é de {area:.2f}m²')
print(f'Para pintar essa parece, você precisa de '
    f'{area/2:.2f}l de tinta')

