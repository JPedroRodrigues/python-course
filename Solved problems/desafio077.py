conjunto = 'guerreiros', 'ponte', 'dourada',\
           'historia', 'jogo', 'mestre', 'pupilo',\
           'servos', 'rena', 'portal', 'raios', 'dinheiro'
for p in conjunto:
    print(f'\nA palavra "{p.upper()}" posssui as vogais: ', end='')
    for v in p:
        if v in 'aeiou':  # A grosso modo, se "v" estiver neste conjunto 'aeiou', mostre-o, senão, nem dê print
            print(v, end=' ')
# Quanto mais funções "for" eu crio envolvendo a variável que eu criei anteriormente, mais fundo é meu nível de extração
# ou seja, se com a variável p eu retirei as strings da tupla, com a variável v eu retiro os caracteres destas strings
for letra_r in conjunto:
    if 'r' in letra_r.lower():
        print(f'\nPalavras com a letra "r": {letra_r} -> Vogais: ', end='')
        for c in letra_r:
            if c in 'aeiou':
                print(c, end=' ')
