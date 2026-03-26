'''numero = int(input('Digite um número inteiro : '))
fatorial = 1
for c in range (numero, 0 , -1):
    fatorial *= c
print(f'O resultado de {numero}! é {fatorial}')'''


numero = int(input('Digite um número inteiro : '))
fatorial = 1
c = numero
while c > 0:
    fatorial *= c
    c -= 1
print(f'O fatorial é {fatorial}')



