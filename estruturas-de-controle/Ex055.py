dados_pessoais=[]
for i in range (0,3):
    print(f'Pessoa {i+1}')
    peso=float(input('Qual é o peso? '))
    dados_pessoais.append(peso)
dados_pessoais.sort()
print(f'A ordem crescente dos pesos é {dados_pessoais[0]:.0f}kg, {dados_pessoais[1]:.0f}kg, {dados_pessoais[2]:.0f}kg.')
