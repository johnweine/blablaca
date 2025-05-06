usr = [{'nome': 'john',
        'email': 'john@gmail.com',
        'senha' : '123'
        }]
usr_carona=[{
    'nome': 'john',
    'local de partida': 'Cajazeiras',
    'destino final': 'Joao pessoa',
    'data' : '04/06/2025'
}]

op= '99'

while op != '0':
    print('----------MENU---------')
    print('1-Cadastrar usurario ')
    print('2-login')
    print('0-sair')

    op = (input('digite a opcao desejada '))


    while True:
        if op == '1':
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
                        'senha': senha
                            }
                            )
                    print('Usuario cadastrado com sucesso')
                    break
                else:
                    print('email invalido por favor digite novamente o email e senha para validação')
                    continue

        elif op == '2':#usuario cadastrado
            op2 = '99'
            while op2 != '3':
                email_val = input('digite seu email:')
                senha_val = input('digite sua senha:')
                for usuario_cada in usr:
                    if usuario_cada['email'] == email_val and usuario_cada['senha'] == senha_val:
                        print('login realizado com sucesso')
                        usuario_cada = True
                        while op2 != '3':
                            print('1-Cadastrar carona')
                            print('2-Pegar carona')
                            print('3-logout')
                            op2 = int(input('Digite a opção que você deseja: '))

                            if op2 == '1':
                                local_origin=input('digite o local de origem: ')
                                local_final=input('digite o destino final: ')

                            elif op2 == '3':
                                break
                            else:
                                print('opção invalida.')
                    else:
                        print('email e senha errado')




        elif op == '0':
            print('Até mais :)')
            break
        elif op == '24': #teste
            print(usr)
            break
        else:
            print('opção invalida! Apenas os números 1, 2 e 3.')
            break
