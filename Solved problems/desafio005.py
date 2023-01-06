cor = {'brancocinza':'\033[1;30;47m', 'vermelhosubli':'\033[4;31m', 'limpa':'\033[m', 'verdebranc':'\033[7;32;40'}
n1 = int(input('{}Me diga um número e eu mostrarei seu sucessor e antecessor:{} '.format(cor['brancocinza'], cor['limpa'])))
print('\033[4;31mÓtimo! Seu sucessor é\33[m \033[7;32;40m{}\033[m \033[4;31me seu antecessor é\033[m '
      '\033[7;32;40m{}\033[m'.format(n1+1, n1-1))
