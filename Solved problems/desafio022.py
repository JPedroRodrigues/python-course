nome = str(input('Digite o seu nome completo: ')).strip()
div = nome.strip().split()
jun = ''.join(div)
print('Em maiúsculo: {}'.format(nome.upper()))
print('Em minúsculo: {}'.format(nome.lower()))
print('Seu nome possui {} letras.'.format(len(jun)))
print('Seu primeiro nome possui {} letras.'.format(len(div[0])))

print('Seu  nome possui {} letras.'.format(len(nome) - nome.count(' ')))
# Neste caso, eu calculo quantos carac. o nome possui menos o número de espaços nele
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
# usei o nome.find(' ') para encontrar o primeiro espaço, que indica a posição deste caractere
# sabendo que a contagem começa do "0", a posição do primeiro espaço indica o número de letras do nome
