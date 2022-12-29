while True:
    deno = int(input('> '))

    #pega o erro para tratar
    try:
        r = 100/deno

    #trata o erro pego no try
    except ZeroDivisionError as erro:
        print('Não rola divisão por zero')

    #executa se o try der certo
    else:
        print(r)
        break
    
    #sempre executa, no acerto e no erro
    finally:
        print('Testando o poder do break')