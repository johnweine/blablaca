usr = [{'nome': 'john',
        'email': 'john@gmail.com',
        'senha' : '123',
        }]
usr_carona=[{
    'nome': 'john',
    'local de partida': 'Cajazeiras',
    'destino final': 'Joao pessoa',
    'data' : '04062025'

}]

op= '99'
usuario_logado= None

while op != '0':
    print('----------MENU---------')
    print('1-Cadastrar usurario ')
    print('2-login')
    print('0-sair')

    op = (input('digite a opcao desejada '))


    if op == '1':
        while True:
            nome = input('digite seu nome')
            email = input('digite o email valido')
            senha = input('digite sua senha')
            email_exis = True
            for email_exis in usr:
                if email_exis['email'] == email:
                    print('Email existente!')
                    continue
                else:
                    email_exis = False
                    break

            if email_exis == False:
                if '@' in email and '.com' in email and '$' not in email and '%' not in email and '&' not in email and '#' not in email and ' ' not in email and '/' not in email and '?' not in email:
                    usr.append({
                        'nome': nome,
                        'email': email,
                        'senha': senha,
                        'logado': False
                            }
                            )
                    print('Usuario cadastrado com sucesso')
                    break
                else:
                    print('email invalido por favor digite novamente o email e senha para validação')
                    continue

    elif op == '2':#usuario cadastrado
        while True:
            email = input('digite seu email:')
            senha = input('digite sua senha:')

            for usuario_cada in usr:
                if usuario_cada['email'] == email and usuario_cada['senha'] == senha:
                    usuario_logado = usuario_cada
                    print('login realizado com sucesso')
                    break
            else:
                print('email e senha errado')
                continue

        while usuario_logado:
            print('1-Cadastrar carona')
            print('2-Pegar carona')
            print('3-logout')
            op2 = (input('Digite a opção que você deseja: '))

            if op2 == '1':
                local_origin=input('digite o local de origem: ')
                local_final=input('digite o destino final: ')
            # elif op2 == '2':
            #     print('')

            elif op2 == '3':
                print('Até mais :)')
                usuario_logado = None
                break
            else:
                print('opção invalida.')


    elif op == '0':
        print('Até mais :)')
        break
    elif op == '24': #teste
        print(usr)
        break
    else:
        print('opção invalida! Apenas os números 1, 2 e 3.')
        break
