nome = input('Me diga o seu nome: ')
print('Prazer em te conhecer {:=^20}!'.format(nome))
n1 = int(input('Me diga um número: '))
n2 = int(input('Diga outro'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
r = n1%n2
print('A soma vale {}, \no produto é {}, \na divisão é {:.3f},'.format(s, m, d), end=' ')
print('a divisão inteira é {}, a fatoração é {} e o resto inteiro é {}'.format(di, e, r))





