# lanche = 'Hambúrguer'
#lanche[1] = 'Manga'  tuple object does not support item assignment (Não é possível assimilar valores em tuplas)
lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Batata-Frita'  # Devo mudar os elementos da tupla manualmente T-T
for comida in lanche:
    print(f'Vou comer {comida}')  # Caso eu não precise de posição
for pos, c in enumerate(lanche):
    print(f'Vou comer {pos}º: {c}')  # Caso eu precise de alguma posição
for a1 in range(0, len(lanche)):
    print(f'Vou comer {a1}º: {lanche[a1]}')  # Caso eu precise de posição, mas com malabarismo mental'''
print(sorted(lanche))  # Perceba que a mudança de ordem não fere a imutabilidade da tupla
a = 1, 2, 3
b = 3, 5, 7, 8, 2
c = a + b
print(c)  # Este caso de soma também não altera os elementos da tupla, mas só junta os termos
print(c.count(2))
print(len(c))
print(c.index(2, 3))
pessoa = 'João', 19, 'M', 53.98  # Tuplas aceitam mais de um tipo de elemento
pessoa2 = 'Alê', 20, 'M', 89.90, 'Itada'
print(pessoa)
del(pessoa2)  # name 'pessoa2' is not defined
del(pessoa[0])  # tuple object doesn't support item deletion - NÃO POSSO MUDAR A TUPLA
fusao = pessoa + pessoa2
print(fusao.index('M', 3))  # Ache 'M' a partir da 3ª posição
