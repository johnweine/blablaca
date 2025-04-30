

usr = []


op= 99
while op != 0:
    print('----------MENU---------')
    print('1-Cadastrar usurario ')
    print('2-login')
    print('0-sair')

    op = int(input('digite a opcao desejada '))
    while True:
        if op == 1:
            nome = input('digite seu nome')
            email = input('digite o email valido')
            senha = input('digite sua senha')

            if '@' in email and '.com' in email and '$' not in email and '%' not in email and '&' not in email and '#' not in email and ' ' not in email:
                usr.append({
                    'nome': nome,
                    'email': email,
                    'senha': senha
                }
                )
                print('Usuario cadastrado com sucesso')
                break
            else:
                print('email invalido por favor digite novamente o email e senha para validação')
                continue
        if op == 2:
            while True:
                email_val = input('digite seu email:')
                senha_val = input('digite sua senha:')
                for usuario_cada in usr:
                    if usuario_cada['email'] == email_val and usuario_cada['senha'] == senha_val:
                        print('login realizado com sucesso')
                    else:
                        print('email e senha errado')
                    print(f'diga seu nome {['nome']} bem vi')





