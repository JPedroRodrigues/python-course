frase = 'Curso em Vídeo Python'.strip()
div = frase.split()
print(div[2][3], 'Vídeo' in div, '-'.join(div))
print(frase.count('o', 0, 15))
print(frase.lower().find('python'))
print(frase.upper().replace('VÍDEO', 'FOCO'))
print(frase.capitalize().split())
print(frase.title().split())
