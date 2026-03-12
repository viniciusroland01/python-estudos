#Progressão aritimética

pt=int(input('Qual o primeiro termo?'))
raz=int(input('Qual a razão? '))
for i in range(10):
    print(pt , end=' → ')
    pt = pt + raz
print('Acabou!')


