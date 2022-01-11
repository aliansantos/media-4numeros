import decimal

print('')
print('Programa simples para calcular a média de 4 números')
print('')
numero1 = decimal.Decimal(input('digite o primeiro número= '))
numero2 = decimal.Decimal(input('digite o segundo número= '))
numero3 = decimal.Decimal(input('digite o terceiro número= '))
numero4 = decimal.Decimal(input('digite o quarto número= '))
print('')
media = (numero1 + numero2 + numero3 + numero4) /4

print('A média é = ',media)