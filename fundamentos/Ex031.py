#Custo de viagem

'''dist=float(input('Qual a distância da viagem? '))
pass1=dist*0.5
pass2=dist*0.45
if dist <= 200:
    print(f'A passagem custará: R$ {pass1:.2f}')
else:
    print(f'A passagem custará: R$ {pass2:.2f}')'''

dist=float(input('Qual a distância da viagem? '))
if dist <= 200:
    preco = 0.50 * dist
else:
    preco = 0.45 * dist
print(f'O valor da passagem é : R${preco:.2f}')

