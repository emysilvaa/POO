class Banco:
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0
        self.titular = None
        path = 'C:\\Users\\20211174010002\\Documents\\POO\\contas.txt'
        with open(path, 'r') as f:
            contas = f.readlines()
        if len(contas) == 0:
            self.titular = input('digite seu nome: ')
            self.saldo = 0
            self.numero = numero
            with open(path, 'a') as f:
                f.write(f'{self.titular}\n')
                f.write(f'{self.numero}\n')
                f.write(f'{self.saldo}\n')
        else:
            for c in contas:
                if f'{self.numero}\n' in contas:
                    print('Conta valida, entrou')
                    break
                else:
                    if self.numero in contas:
                        print('Já existe')
                        break
                    else:
                        self.titular = input('digite seu nome: ')
                        self.saldo = 0
                        self.numero = numero
                        with open(path, 'a') as f:
                            f.write(f'{self.titular}\n')
                            f.write(f'{self.numero}\n')
                            f.write(f'{self.saldo}\n')
                        break

    def verificarSaldo(self):
        path = 'C:\\Users\\20211174010002\\Documents\\POO\\contas.txt'
        with open(path, 'r') as f:
            contas = f.readlines()
        cont = 0
        for c in contas:
            if f'{self.numero}\n' == c:
                break
            cont+=1
        self.saldo = contas[cont+1]
        print(self.saldo)

    def depositar(self, valor):
        path = 'C:\\Users\\20211174010002\\Documents\\POO\\contas.txt'
        with open(path, 'r') as f:
            contas = f.readlines()
        cont = 0
        for c in contas:
            if f'{self.numero}\n' == c:
                break
            cont+=1
        self.saldo = contas[cont+1]
        num = ''
        for c in self.saldo:
            if c != '\n':
                num += c
        self.saldo = int(num)
        self.saldo += valor
        cont1 = 0
        for c in contas:
            if f'{self.numero}\n' == c:
                break
            cont1+=1
        contas[cont1+1] = f'{self.saldo}\n'
        with open(path, 'w') as f:
            f.writelines(contas)
    
    def transferir(self, valor, destino):
        path = 'C:\\Users\\20211174010002\\Documents\\POO\\contas.txt'
        with open(path, 'r') as f:
            contas = f.readlines()
        cont = 0
        for c in contas:
            if f'{self.numero}\n' == c:
                break
            cont+=1
        self.saldo = contas[cont+1]
        num = ''
        for c in self.saldo:
            if c != '\n':
                num += c
        self.saldo = int(num)
        self.saldo -= valor
        cont1 = 0
        for c in contas:
            if destino == c:
                break
            cont1+=1
        self.saldo = contas[cont1+1]
        num = ''
        for c in self.saldo:
            if c != '\n':
                num += c
        self.saldo = int(num)
        self.saldo += valor
        
eu = Banco(123)
eu.verificarSaldo()
eu.transferir(200, 312)