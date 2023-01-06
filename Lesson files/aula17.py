n = [4, 5, 6, 1, 6, 9, 0, 7, 6, 6, 6]
print(f'Lista original: {n} --> {len(n)} elementos')
n.sort()
n.pop()
n.sort(reverse=True)
n.remove(7)
del n[4]
n.insert(5, 8)
print(f'Lista modificada: {n} --> {len(n)} elementos')
print(f'Maior: {max(n)}\nMenor: {min(n)}')
print(f'Remoção automática do nº6 com a função for: ', end='')
while True:
    if 6 in n:
        n.remove(6)
    elif 6 not in n:
        break
for c in n:
    print(c, end=' ')
print(f'\nMaior 2.0: {max(n)}\nMenor 2.0: {min(n)}\nNº de elementos: {len(n)}')
for p, v in enumerate(n):
    print(f'Na posição {p} encontrei o elemento {v}')
a = list(range(6, 13))  # Lista do 6 ao 12
b = a
b[0] = 999  # Se você iguala duas listas, tudo o que você mexe em uma, você mexe na outra
# b = a[:] tenho que b recebe todos os valores de a, o que realiza uma cópia de outra lista, não há ligação
print(f'Lista A: {a}')
print(f'Lista B: {b}')
c = list(range(1, 7))
d = c[:]  # Criei uma cópia de uma lista c e atribui ela a d - b recebe os elementos de c
d[0] = 999
print(f'Lista C: {c}')
print(f'Lista D: {d}')
