#Reajuste salarial

f=float(input('Quanto recebe o funcionário? '))
a=float(input('De quanto será o aumento? '))
s=f+(f*(a/100))
print(f'O funcionário que recebia R${f} com aumento de {a}% passará a receber R${s:.2f}. ')