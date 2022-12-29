path = 'C:\\Users\\20211174010002\\Documents\\POO\\provinha\\dados.txt'
try:
    with open(path, 'r') as f:
        dados = f.readlines()
except:
    with open(path, 'w') as f:
        f.write('')

nome = input('nome > ')
sexo = input('sexo > ')
endereco = input('endereco > ')
cidade = input('cidade > ')
estado = input('estado > ')

with open(path, 'a') as f:
    f.write(nome + '@' + sexo + '@' + endereco + '@' + cidade + '@' + estado + '\n')