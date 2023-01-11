from urllib import request, error
try:
    link = request.urlopen('https://audaces.com/')
except error.HTTPError:
    print('\033[31mErro de HTTP\033[m')
except error.URLError:
    print('\033[31mOps! Não foi possível acessar o site.\033[m')
else:
    print(f'\033[32mO site "https://audaces.com/" se encontra acessível no momento.\033[m')
finally:
    print('Volte sempre!')
