cor = {'azul': '\033[1;34m', 'l': '\033[m'}
print('{}IDENTIFICADOR DE PALÍNDROMOS{}'.format(cor['azul'], cor['l']))
print('Por favor, não utilize acentuação nas palavras, nem pontuação (vírgulas, reticências, pontos)')
for c in range(1, 4):
    frase = str(input('Digite a {}° frase/palavra: '.format(c))).strip().lower()
    forma = frase.split()
    uniao = ''.join(forma)
    if uniao == uniao[::-1]:
        print('É um palíndromo!')
        print('Observe: "{}" e "{}".'.format(uniao, uniao[::-1]))
    else:
        print('Não, "{}" não é um palíndromo...'.format(frase))
