#Calculando descontos

p=float(input('Qual o valor do produto? R$'))
d=float(input('Qual a porcentagem do desconto? (/100) '))
pf=p- (p*(d/100))
print(f'O produto que custa {p}R$, na promoção com {d}% de desconto custará: {pf:.2f}R$.')
