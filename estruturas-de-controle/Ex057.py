s = 25
c = int(input('Tente acertar o número do programa : '))

'''while c != s:
    c = int(input('Tente novamente! '))
print('Parabéns!')'''

while True:

    if c != s:
        c = int(input('Tente novamente!'))
    elif c == s:
        print('Parabéns!')
        break


