num=int(input('Digite o primeiro termo: '))
raz=int(input('Digite a razão: '))

quantidade = 0
mais = 10
total= 0

while mais != 0 :

    total += mais

    while quantidade < total:
        print(num , end=' → ')
        num += raz
        quantidade += 1
    print('Fim!')

    mais=int(input('Quantos termos a mais você quer ver? '))

print('Acabou!')



