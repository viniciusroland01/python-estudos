#Maior e menor da sequência

''''dados_pessoais = []
for i in range (1,6):
    peso = float(input(f'Qual é o peso da {i}ª pessoa? '))
    dados_pessoais.append(peso)
dados_pessoais.sort()
print(f'A ordem crescente dos pesos é {dados_pessoais[0]:.1f}kg, {dados_pessoais[1]:.1f}kg, {dados_pessoais[-1]:.1f}kg.')
print(f'O maior peso lido foi {dados_pessoais[-1]:.1f}kg e o menor peso {dados_pessoais[0]:.1f}kg')'''

maior=0
menor=0
for p in range (1,6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}, e o menor é {menor}')
