from random import randint
from time import sleep
print(f'\n{"| PALPITES PARA MEGA SENA |":=^50}')
palpite = []
mega = []
perg = int(input('Quantos jogos você pretende fazer? '))
for jogos in range(perg):
    while len(palpite) != 6:
        palpite.append(randint(1, 60))
        if palpite.count(palpite[-1]) == 2:
            palpite.pop()
    palpite.sort()
    mega.append(palpite[:])
    palpite.clear()
print(f'{"| NÚMEROS SORTEADOS |":=^50}')
sleep(1)
for pos, lista in enumerate(mega):
    print(f'Jogo {pos+1}: {lista}')
    sleep(1)
print(f'{"| BOA SORTE! |":=^50}')
