def voto(ano):
    """
    -> Informa se o cidadão possui a obrigatoriedade de votar nas próximas eleições políticas.
    :param ano: Ano de nascimento do cidadão.
    :return: Retorna a situação eleitoral.
    """
    from datetime import datetime
    atual = datetime.now().year
    idade = atual - ano
    if 18 <= idade < 65:
        return f'Completa {idade} anos em {atual}. Neste caso, o voto é obrigatório.'
    elif idade >= 65 or 16 <= idade < 18:
        return f'Completa {idade} anos em {atual}. Neste caso, o voto é facultativo.'
    else:
        return f'Cidadãos que apresentam {idade} ano(s) de idade não têm o direito de votar.'


# Programa principal
print('-'*40)
birth = int(input('Digite o seu ano de nascimento: '))
print(voto(birth))
