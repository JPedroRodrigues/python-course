# Exercício sobre inserção correta de parênteses em expressões matemáticas
expresion = '(3*(a+b))/2'
expresion1 = 'ab+c)-(g'
# Preciso checar a compatibilidade dos parênteses, não somente o números dele
# Importa mais a compatibilidade, a ordem dos parênteses, do que somente os números deles
exp = str(input('Digite uma expressão matemática: ')).strip()
lista = []
for p in exp:  # "Destrincho" os elementos da nossa expressão, que, por ser str, é uma lista por si só
    if p == '(':
        lista.append(p)  # Caso um parênteses aberto for encontrado, ele, e somente ele, será inserido na lista
    elif p == ')':  # Se o encontrado for fechado, eu preciso pensar em uma coisa:
        if len(lista) == 0:  # Existia um elemento na lista, ou não (sabendo que ela só comporta os abertos)?
            lista.append(')')  # Se não tiver, eu adiciono o fechado e termino o looping imediatamente
            break
        elif len(lista) > 0:  # Se o tamanho da lista for maior que zero, significa que existe um aberto lá
            lista.pop()  # Assim, eu elimino o elemento aberto que é compatível com o p. fechado encontrado
if len(lista) == 0:  # A lista, para descrever um acerto, precisa ter nenhum elemento em sua posição
    print(f'Sua expressão foi escrita corretamente.')
else:
    print(f'Expressão, "{exp}", escrita erroneamente.')
#  Esse é um bom meio de averiguar a existência de elementos "pares" - ou compatíveis.
#  A peculiaridade deste caso está no fato de que eu analiso a ordem em que os parênteses foram colocados
#  A ordem, na  matemática, para os parênteses importa muito.
