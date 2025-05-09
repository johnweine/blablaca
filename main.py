usr = [{'nome': 'john',
        'email': 'john@gmail.com',
        'senha': '123'
        },
       {'nome': 'lorran',
        'email': 'lorran@.com',
        'senha': '123'
        }]

usr_carona = [{
    'nome': 'john',
    'local de partida': 'CZ',
    'destino final': 'JP',
    'dia': 4,
    'mes': 6,
    'ano': 2024,
    'horario': '12:00',
    'vagas': 4,
    'valor por vaga': 200.0,
    'passageiros':[]
},
    {'nome': 'lorran',
     'local de partida': 'CZ',
     'destino final': 'JP',
     'dia': '15',
     'mes': '8',
     'ano': '2025',
     'horario': '22:00',
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
            if '@' in email and '.com' in email and not any(c in email for c in ['$', '%', '&', '#', ' ', '/', '?']):
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
                print('---------------------- DE CARONAS ---------------------')
                print('-------------------------------------------------------')
                print('                                                       ')
                print('1-CADASTRAR CARONA')
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
                        if dia <= 31 and dia >= 1 and mes in[1, 3, 5, 7, 8,10,12]:
                            print('meses com 31 dias')
                            break
                        elif dia <= 30 and dia >= 1 and mes in [4, 6, 9, 11]:
                            print('mes com 30 dias')
                            break
                        elif ano % 4 == 0 and dia >= 1 and dia <= 29 and mes == 2:
                            break
                        elif ano % 4 != 0 and dia >= 1 and dia <= 28 and mes == 2:
                            break
                        else:
                            print('data invalida')
                            continue
                    while True:
                        horario = input('Digite o horário da carona (HH:MM): ')

                        if ':' in horario:
                            partes = horario.split(':')
                            if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
                                horas = int(partes[0])
                                minutos = int(partes[1])
                                if 0 <= horas < 24 and 0 <= minutos < 60:
                                    break

                        print('Horário inválido! Use o formato HH:MM com valores válidos.')
                    vagas = int(input('digite a quantidade de vagas: '))
                    valor = float(input('digite o valor por vaga: '))


                    usr_carona.append({
                        'nome': usuario_logado['nome'],
                        'email': usuario_logado['email'],
                        'local de partida': local_origin,
                        'destino final': local_final,
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
                        print('TODAS AS CARONAS DISPONÍVEIS:')
                        for i, carona in enumerate(usr_carona, 1):
                            print(f"\nCARONA {i}:")
                            print(
                                f"Motorista: {carona['nome']} \n Local de Partida: {carona['local de partida']} \n Destino Final: {carona['destino final']} \n Data: {carona['dia']} / {carona['mes']} / {carona['ano']} \n Horário: {carona['horario']} \n Vagas: {carona['vagas']} \n Valor por vaga: R${carona['valor por vaga']:.2f}")
                            print('                                                       ')

                elif op2 == '3':
                    while True:
                        if len(usr_carona) > 1:
                            origem_busca = input('Digite a origem desejada: ')
                            destino_busca = input('Digite o destino desejado: ')

                            caronas_encontradas = False

                            print('\nRESULTADOS DA BUSCA:')
                            print('-------------------------------------------------------')
                            for i, carona in enumerate(usr_carona, 1):
                                if (origem_busca in carona['local de partida'] and
                                        destino_busca in carona['destino final'] and
                                        carona['vagas'] > 0):
                                    print(
                                        f"Motorista: {carona['nome']} \n Local de Partida: {carona['local de partida']} \n Destino Final: {carona['destino final']} \n Data: {carona['dia']} / {carona['mes']} / {carona['ano']} \n Horário: {carona['horario']} \n Vagas: {carona['vagas']} \n Valor por vaga: R${carona['valor por vaga']:.2f}")
                                    print('                                                       ')
                                    caronas_encontradas = True

                        elif not caronas_encontradas:
                            print('\nNENHUMA CARONA ENCONTRADAD PARA ESSE DESTINO ESPECIFICO.')
                            print('-------------------------------------------------------')
                        else:
                            print('-------------------------------------------------------')
                            print('              NENHUM CADASTRO NO MOMENTO              ')
                            print('-------------------------------------------------------')
                            break

                elif op2 == '4':
                    if len(usr_carona) == 0:
                        print('-------------------------------------------------------')
                        print('              NENHUMA CARONA DISPONÍVEL               ')
                        print('-------------------------------------------------------')
                    else:
                        print('Caronas disponíveis:')
                        for i, carona in enumerate(usr_carona, 1):
                            if carona['vagas'] > 0:
                                print(
                                    f"{i}. Motorista: {carona['nome']} - {carona['local de partida']} para {carona['destino final']} em {carona['dia']}/{carona['mes']}/{carona['ano']} às {carona['horario']}")

                        escolha_input = input('Escolha o número da carona que deseja reservar: ')

                        if escolha_input.isdigit():
                            escolha = int(escolha_input) - 1
                            if 0 <= escolha < len(usr_carona):
                                carona = usr_carona[escolha]
                                if carona['vagas'] > 0:
                                    if 'passageiros' not in carona:
                                        carona['passageiros'] = []
                                    if usuario_logado['email'] in carona['passageiros']:
                                        print('Você já reservou uma vaga nesta carona!')
                                    else:
                                        carona['vagas'] -= 1
                                        carona['passageiros'].append(usuario_logado['email'])
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

    if op == '0':
        print('SAINDO DO SISTEMA ATE BREVE! ...')
    if op == '24':
        print(usr)
        break
