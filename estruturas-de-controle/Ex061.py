num=int(input('Digite o primeiro termo: '))
raz=int(input('Digite a razão: '))
quantidade= 0
while quantidade < 10:
    print(num , end=' → ')
    num = num + raz
    quantidade += 1
print('Acabou!')