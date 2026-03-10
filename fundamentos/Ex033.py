#Maior e menor valores

n1=float(input('Digite o primeiro número'))
n2=float(input('Digite o segundo número'))
n3=float(input('Digite o terceiro número'))
lista=n1,n2,n3
maior=max(lista)
menor=min(lista)
print(f'O maior número é {maior:.0f} e o menor é {menor:.0f}')