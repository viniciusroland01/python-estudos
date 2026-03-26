num = int(input('Digite um valor ou "999" para sair : '))
quantidade = 0
soma = 0

while num != 999 :
    soma += num
    num = int(input('Digite um valor ou "999" para parar : '))
    quantidade += 1

print(f'Foram digitados {quantidade} números e a soma deles é {soma}.')