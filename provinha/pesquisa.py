path = 'C:\\Users\\20211174010002\\Documents\\POO\\provinha\\pesquisa.txt'

with open(path, 'r') as f:
    dados = f.readlines()

for c in dados:
    p = c.split('-#-')
    if p[1] == 'natal\n' or p[1] == 'natal':
        print(p[0])


    






