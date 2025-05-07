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
    op = (input('DIGITE A OPÇÃO DESEJADA - '))
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

            if not False != email_exis:
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
        while True:
            print('-------------------------------------------------------')
            print('-------------------- MENU DE LOGIN --------------------')
            print('-------------------------------------------------------')
            print('    ')
            email = input('DIGITE O SEU EMAIL: ')
            senha = input('DIGITE SUA SENHA: ')

            for usuario_cada in usr:
                if usuario_cada['email'] == email and usuario_cada['senha'] == senha:
                    usuario_logado = usuario_cada
                    print('LOGIN REALIZADO COM SUCESSO')
                    print('  ')

                    op = 99
                    while op != 0:
                        print('-------------------------------------------------------')
                        print('-------------- MENU DE CARONAS E CADASTRO -------------')
                        print('---------------------- DE CARONAS ---------------------')
                        print('-------------------------------------------------------')
                        print('                                                       ')
                        print('1-CADASTRAR CARONA')
                        print('2-LISTAR TODAS AS CARONAS DISPONÍVEIS')
                        print('3-BUSCAR CARONA POR ORIGEM E DESTINO')
                        print('4-LOGOUT')
                        print('                                                       ')
                        print('-------------------------------------------------------')
                        print('-------------------------------------------------------')


                        op2 = input('DIGITE A OPÇÃO DESEJADA - ')




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
                            if len(usr_carona) == 0:  # Ver se a lista ta vazia
                                print('                                                       ')
                                print('-------------------------------------------------------')
                                print('--------- NENHUM CARONA DISPONIVEL NO MOMENTO ---------')
                                print('-------------------------------------------------------')
                                print('                                                       ')


                            elif op2 == '2':
                                print('TODAS AS CARONAS DISPONÍVEIS:')
                                for i, carona in enumerate(usr_carona, 1):
                                    print(f"\nCARONA {i}:")
                                    print(
                                        f"Motorista: {carona['nome']} \n Local de Partida: {carona['local de partida']} \n Destino Final: {carona['destino final']} \n Data: {carona['data']} \n Horário: {carona['horario']} \n Vagas: {carona['vagas']} \n Valor por vaga: R${carona['valor por vaga']:.2f}")
                                    print('                                                       ')

                        elif op2 == '3':
                            if len(usr_carona) == 0:
                                print('-------------------------------------------------------')
                                print('              NENHUM CADASTRO NO MOMENTO              ')
                                print('-------------------------------------------------------')
                            else:
                                origem_busca = input('Digite a origem desejada: ').strip().lower()
                                destino_busca = input('Digite o destino desejado: ').strip().lower()

                                caronas_encontradas = False

                                print('\nRESULTADOS DA BUSCA:')
                                print('-------------------------------------------------------')
                                for i, carona in enumerate(usr_carona, 1):
                                    if (origem_busca in carona['local de partida'].lower() and
                                            destino_busca in carona['destino final'].lower() and
                                            carona['vagas'] > 0):
                                        print(f"\nCARONA {i}:")
                                        print(f"Motorista: {carona['nome']}")
                                        print(f"Local de Partida: {carona['local de partida']}")
                                        print(f"Destino Final: {carona['destino final']}")
                                        print(f"Data: {carona['data']}")
                                        print(f"Horário: {carona['horario']}")
                                        print(f"Vagas disponíveis: {carona['vagas']}")
                                        print(f"Valor por vaga: R${carona['valor por vaga']:.2f}")
                                        caronas_encontradas = True

                            if caronas_encontradas:
                                print('\nNENHUMA CARONA ENCONTRADAD PARA ESSE DESTINO ESPECIFICO.')
                            print('-------------------------------------------------------')

                        elif op2 == '4':
                            print('                             ')
                            print('SAINDO DO MENU DE CARONA ... ')
                            print('                             ')
                            break



            if not usuario_logado:
                print('email ou senha errados')

    if op == 0:
        print('Saindo do sistema...')

