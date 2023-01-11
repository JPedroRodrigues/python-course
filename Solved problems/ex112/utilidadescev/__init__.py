def leiaDinheiro(prompt=None):
    while True:
        valor = str(input(prompt)).replace(',', '.').strip()
        if valor.isdigit() or valor.replace('.', '').isdigit() and valor.count('.') == 1:
            break
        else:
            print(f'\033[31mErro! \"{valor}\" não é considerado um número.\033[m')
    return float(valor)

