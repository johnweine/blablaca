usr = [{'nome': 'john',
        'email': 'john@gmail.com',
        'senha': '123'
        },
       {'nome': 'lorran',
        'email': 'lorran@.com',
        'senha': '123'
        },
       {'nome': 'cleiton',
        'email': '@.com',
        'senha': '123'
        }
       ]

usr_carona = [{
    'nome': 'john',
    'local de partida': 'cz',
    'destino final': 'jp',
    'dia': 4,
    'mes': 6,
    'ano': 2024,
    'horario': '12',
    'vagas': 4,
    'valor por vaga': 200.0,
    'passageiros':[]
},
    {'nome': 'lorran',
     'local de partida': 'cz',
     'destino final': 'jp',
     'dia': '15',
     'mes': '8',
     'ano': '2025',
     'horario': '22',
     'vagas': 2,
     'valor por vaga': 225.0,
     'passageiros': []
     }]

op = '99'
usuario_logado = None

while op != '0':
    print('-------------------------------------------------------')
    print('------------------ MENU PRINCIPAL ---------------------')
    print('--------------------- BLABLACA ------------------------')
    print('-------------------------------------------------------')
    print('                                                       ')
    print('1-CADASTRA USUARIO ')
    print('2-LOGIN')
    print('3-SAIR')
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

            # Verificar se email já existe
            email_existente = False
            for usuario in usr:
                if usuario['email'] == email:
                    email_existente = True
                    break

            if email_existente:
                print('Email já cadastrado!')
                continue

            # Validar formato do email
            if '@' in email and '.com' in email and '$' not in email and '%' not in email and '&' not in email and '#' not in email and ' ' not in email and '/' not in email and '?' not in email:
                usr.append({
                    'nome': nome,
                    'email': email,
                    'senha': senha,
                })
                print('---- USUARIO CADASTRADO COM SUCESSO ----')
                break
            else:
                print('Email inválido! Por favor digite novamente.')

    elif op == '2':  # usuario cadastrado
        op2 = '99'
        while op2 != '0':
            print('-------------------------------------------------------')
            print('--------------- TELA DE LOGIN BLABLACAR ---------------')
            print('-------------------------------------------------------')
            print('    ')
            email = input('EMAIL: ')
            senha = input('SENHA: ')

            for usuario_cada in usr:
                if usuario_cada['email'] == email and usuario_cada['senha'] == senha:
                    usuario_logado = usuario_cada
                    print('LOGIN REALIZADO COM SUCESSO')
                    print('  ')
                    break

            else:
                print('Email e senha incorreto!')

            while usuario_logado:
                print('-------------------------------------------------------')
                print('-------------- MENU DE CARONAS E CADASTRO -------------')
                print('----------------------DE CARONAS-----------------------')
                print('-------------------------------------------------------')
                print('                                                       ')
                print(f'BEM VINDO: {usuario_logado['nome'].upper()}')
                print('\n1-CADASTRAR CARONA')
                print('2-LISTAR TODAS AS CARONAS DISPONÍVEIS')
                print('3-BUSCAR CARONA POR ORIGEM E DESTINO')
                print('4-RESERVAR VAGA EM CARONA')
                print('5-LOGOUT')
                print('                                                       ')
                print('-------------------------------------------------------')
                print('-------------------------------------------------------')

                op2 = input('DIGITE A OPÇÃO DESEJADA - ')

                if op2 == '1':
                    local_origin = input('digite o local de origem: ')
                    local_final = input('digite o destino final: ')
                    while True:
                        dia = int(input('digite o dia da carona '))
                        mes = int(input('digite o mes da carona '))
                        ano = int(input('digite o ano da carona'))
                        if   31 >= dia >= 1 and mes in[1, 3, 5, 7, 8,10,12]:
                            break
                        elif 30 >= dia >= 1 and mes in [4, 6, 9, 11]:
                            break
                        elif ano % 4 == 0 and dia >= 1 and dia <= 29 and mes == 2:
                            break
                        elif ano % 4 != 0 and dia >= 1 and dia <= 28 and mes == 2:
                            break
                        else:
                            print('data invalida')
                            continue
                    horario = input('Digite o horário da carona (HH:MM): ')
                    vagas = int(input('digite a quantidade de vagas: '))
                    if vagas < 0:
                        print('Vagas invalidas')
                    valor = float(input('digite o valor por vaga: '))
                    if valor < 0:
                        print('Valor invalido')


                    usr_carona.append({
                        'nome': usuario_logado['nome'],
                        'email': usuario_logado['email'],
                        'local de partida': local_origin.lower(),
                        'destino final': local_final.lower(),
                        'dia': dia,
                        'mes': mes,
                        'ano': ano,
                        'horario': horario,
                        'vagas': vagas,
                        'valor por vaga': valor,
                        'passageiros': []
                    })
                    print('CARONA CADASTRADA COM SUCESSO!')
                    print('              ')

                elif op2 == '2':
                    if len(usr_carona) == 0:  # Ver se ta vazia
                        print('                                                       ')
                        print('-------------------------------------------------------')
                        print('--------- NENHUMA CARONA DISPONIVEL NO MOMENTO ---------')
                        print('-------------------------------------------------------')
                        print('                                                       ')

                    elif len(usr_carona) > 0:
                        i = 1
                        qtd = 0
                        print('TODAS AS CARONAS DISPONÍVEIS:')
                        for carona in usr_carona:
                            if carona['nome'] == usuario_logado['nome']:
                                qtd =+ 1
                                continue
                            if qtd == 0:
                                print(f"\nCARONA {i}:")
                                print(
                                    f"Motorista: {carona['nome']} \n Local de Partida: {carona['local de partida']} \n Destino Final: {carona['destino final']} \n Data: {carona['dia']} / {carona['mes']} / {carona['ano']} \n Horário: {carona['horario']}:00 \n Vagas: {carona['vagas']} \n Valor por vaga: R${carona['valor por vaga']:.2f}")
                                print('                                                       ')
                                i += 1

                            else:
                                print(f"\nCARONA {i}:")
                                print(
                                    f"Motorista: {carona['nome']} \n Local de Partida: {carona['local de partida']} \n Destino Final: {carona['destino final']} \n Data: {carona['dia']} / {carona['mes']} / {carona['ano']} \n Horário: {carona['horario']} \n Vagas: {carona['vagas']} \n Valor por vaga: R${carona['valor por vaga']:.2f}")
                                print('                                                       ')

                        pulo = input('Deseja reserva 1 vaga? Digite (S/N) ').upper()

                elif op2 == '3':
                    while True:
                        if len(usr_carona) > 1:
                            origem_busca = input('Digite a origem desejada: ').lower()
                            destino_busca = input('Digite o destino desejado: ').lower()

                            caronas_encontradas = False

                            print('\nRESULTADOS DA BUSCA:')
                            print('-------------------------------------------------------')
                            for carona in usr_carona:
                                if (origem_busca in carona['local de partida'] or destino_busca in carona['destino final'] and carona['vagas'] > 0):
                                    print(
                                        f"Motorista: {carona['nome']} \n Local de Partida: {carona['local de partida']} \n Destino Final: {carona['destino final']} \n Data: {carona['dia']} / {carona['mes']} / {carona['ano']} \n Horário: {carona['horario']} \n Vagas: {carona['vagas']} \n Valor por vaga: R${carona['valor por vaga']:.2f}")
                                    print('                                                       ')
                                    caronas_encontradas = True



                        elif not caronas_encontradas:
                            print('\nNENHUMA CARONA ENCONTRADAD PARA ESSE DESTINO ESPECIFICO.')
                            print('-------------------------------------------------------')
                            break
                        else:
                            print('-------------------------------------------------------')
                            print('              NENHUM CADASTRO NO MOMENTO              ')
                            print('-------------------------------------------------------')
                            break
                        break

                elif op2 == '4':#Reservar carona
                    if len(usr_carona) == 0:
                        print('-------------------------------------------------------')
                        print('              NENHUMA CARONA DISPONÍVEL               ')
                        print('-------------------------------------------------------')
                    else:
                        i = 1
                        print('Caronas disponíveis:')
                        for carona in usr_carona:
                            if carona['vagas'] > 0:
                                print(f"{i}. Motorista: {carona['nome']} - {carona['local de partida']} para {carona['destino final']} em {carona['dia']}/{carona['mes']}/{carona['ano']} às {carona['horario']}:00 \n {carona['vagas']} ")
                                i += 1

                        reserva = int(input('Escolha o número da carona que deseja reservar: '))

                        if reserva:
                            escolha = reserva - 1
                            if 0 <= escolha < len(usr_carona):
                                carona = usr_carona[escolha]
                                if carona['vagas'] > 0:
                                    if usuario_logado['nome'] in carona['passageiros']:
                                        print('Você já reservou uma vaga nesta carona!')
                                    else:
                                        carona['vagas'] -= 1
                                        carona['passageiros'].append(usuario_logado['nome'])
                                        print('Vaga reservada com sucesso!')
                                else:
                                    print('Não há vagas disponíveis nesta carona.')
                            else:
                                print('Número de carona inválido!')
                        else:
                            print('Por favor, digite um número válido.')


                elif op2 == '5':
                    print('                             ')
                    print('SAINDO DO MENU DE CARONAS ... ')
                    print('                             ')
                    op2 = '0'
                    usuario_logado = None
                else:
                    print('OPÇÃO INVALIDA!')

    elif op == '0':
        print('SAINDO DO SISTEMA ATE BREVE! ...')

    if op == '24':
        print(usr)
        break
    if op =='69':
        print(usr_carona)
    else:
        print('OPÇÃO INVALIDA')