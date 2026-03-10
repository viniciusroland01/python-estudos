#Aprovando empréstimo

casa=float(input('Qual o valor da casa? R$'))
salario=float(input('Qual o seu salário? R$'))
tempo=int(input('Quantos anos será concluído o pagamento? '))
ano=tempo*12
prestacao=casa/ano
if prestacao >= 0.3 * salario:
    print('O empréstimo foi negado!')
    print(f'Você precisaria receber no mínimo R${prestacao / 0.3:.2f}')
else:
    print('O empréstimo foi aprovado!')
print(f'Para pagar uma casa de R${casa:.2f} em {tempo} anos a prestação será de R${prestacao:.2f}')
