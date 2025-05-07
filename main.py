usr = [{'nome': 'john',
        'email': 'john@gmail.com',
        'senha' : '123'
        },
       {'nome': 'lorran',
        'email': 'lorran@.com',
        'senha': '123'
        }]

usr_carona = []

op= '99'
usuario_logado= None

while op != '0':
    print('-------------------------------------------------------')
    print('------------------ MENU PRINCIPAL ---------------------')
    print('--------------------- BLABLACA ------------------------')
    print('-------------------------------------------------------')
    print('                                                       ')
    print('1-CADASTRA USUARIO ')
    print('2-LOGIN')
    print('0-SAIR')
    print('                                                       ')
    print('-------------------------------------------------------')
    print('-------------------------------------------------------')
    print('                                                       ')
    op = (input('---- DIGITE A OPÇÃO DESEJADA ---- '))
    print('                                                       ')


    if op == '1':
        while True:
            nome = input('DIGITE SEU NOME: ')
            email = input('DIGITE O EMAIL VALIDO: ')
            senha = input('DIGITE SUA SENHA: ')
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
                    print('---- USUARIO CADASTRADO COM SUCESSO ----')
                    break
                else:
                    print('email invalido por favor digite novamente o email e senha para validação')
                    continue

    elif op == '2':#usuario cadastrado
        # while True:
            print('---------- MENU DE LOGIN ----------')
            email = input('DIGITE O SEU EMAIL: ')
            senha = input('DIGITE SUA SENHA: ')

            for usuario_cada in usr:
                if usuario_cada['email'] == email and usuario_cada['senha'] == senha:
                    usuario_logado = usuario_cada
                    print('LOGIN REALIZADO COM SUCESSO')
                    print('  ')
                    break

            while usuario_logado:
                print('-------------------------------------------------------')
                print('-------------- MENU DE CARONAS E CADASTRO -------------')
                print('---------------------- DE CARONAS ---------------------')
                print('-------------------------------------------------------')
                print('                                                       ')
                print('1-CADASTRAR CARONA')
                print('2-PEGAR CARONA')
                print('3-LOGOUT')
                print('                                                       ')
                print('-------------------------------------------------------')
                print('-------------------------------------------------------')

                op2 = input('---- DIGITE A OPÇÃO DESEJADA ---- ')

                if op2 == '1':
                    local_origin = input('digite o local de origem: ')
                    local_final = input('digite o destino final: ')
                    data = input('digite a data da carona (dd/mm/yyyy): ')
                    horario = input('digite o horário da carona (HH:MM): ')
                    vagas = int(input('digite a quantidade de vagas: '))
                    valor = float(input('digite o valor por vaga: '))

                    usr_carona.append({
                        'nome': usuario_cada['nome'],  # Nome do motorista
                        'local de partida': local_origin,
                        'destino final': local_final,
                        'data': data,
                        'horario': horario,
                        'vagas': vagas,
                        'valor por vaga': valor
                    })
                    print('CARONA CADASTRADA COM SUCESSO!')
                    print('              ')

                elif op2 == '2':
                    print('CARONAS DISPONIVEIS:')
                    for carona in usr_carona:
                        print(
                            f"Motorista: {carona['nome']} \n Local de Partida: {carona['local de partida']} \n Destino Final: {carona['destino final']} \n Data: {carona['data']} \n Horário: {carona['horario']} \n Vagas: {carona['vagas']} \n Valor por vaga: R${carona['valor por vaga']:.2f}")
                        print('                                                       ')


                elif op2 == '3':
                    print('Até mais :)')
                    usuario_logado = None
                    break
            else:
                print('email ou senha errado!')


    if op == 0:
        print('Saindo do sistema...')
    else:
        print('opção invalida! Digite apenas os numeros 1, 2 e 3.')
