import os
from utils import *

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
    'email': 'john@gmail.com',
    'local de partida': 'cz',
    'destino final': 'jp',
    'dia': '4',
    'mes': '6',
    'ano': '2025',
    'horario': '12',
    'vagas': 4,
    'valor por vaga': 200.0,
    'modelo':'camaro amarelo',
    'detalhe': 'Ira passar por sao ze',
    'passageiros': []
},
    {'nome': 'lorran',
     'email': 'lorran@.com',
     'local de partida': 'cz',
     'destino final': 'jp',
     'dia': '15',
     'mes': '8',
     'ano': '2025',
     'horario': '22',
     'vagas': 2,
     'valor por vaga': 225.0,
     'detalhe': 'ira passar por triunfo',
     'modelo': 'toyata SW4',
     'passageiros': []
     }]

carros = [{
    'black1': 'Mercedes-Benz S-Class',
    'black2': 'BMW 7 Series',
    'black3': 'Audi A8',
    'premium1': 'Toyota Camry',
    'premium2': 'Hyundai Sonata',
    'premium3': 'Honda Accord',
    'classic1': 'Celta',
    'classic2': 'Mobi',
    'classic3': 'Gol',
    'outro': ''
}]

op = '99'
usuario_logado = None

while op != '0':
    menu_principal('MENU PRINCIPAL')
    op = (input('DIGITE A OPÇÃO DESEJADA - '))

    if op == '1':
        while True:
            nome = input('DIGITE SEU NOME: ')
            email = input('DIGITE O EMAIL VALIDO: ')
            senha = input('DIGITE SUA SENHA: ')


            email_existente = False
            for usuario in usr:
                if usuario['email'] == email:
                    email_existente = True
                    break

            if email_existente:
                print('Email já cadastrado!')
                continue


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

    elif op == '2':
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
                print('5-CANCELAR RESERVA')
                print('6-LOGOUT')
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
                        if 31 >= dia >= 1 and mes in [1, 3, 5, 7, 8, 10, 12]:
                            break
                        elif 30 >= dia >= 1 and mes in [4, 6, 9, 11]:
                            break
                        elif ano % 4 == 0 and dia >= 1 and dia <= 29 and mes == 2:
                            break
                        elif ano % 4 != 0 and dia >= 1 and dia <= 28 and mes == 2:
                            break
                        if 2025 >= ano <= 3000:
                            break
                        else:
                            print('data invalida')
                            continue
                    horario = input('Digite o horário da carona (HH): ')
                    vagas = int(input('Digite a quantidade de vagas: '))
                    detalhe = input('Digite o detalhe da viagem')

                    print('\nESCOLHA A CLASSE DO VEICULO:')
                    print('1 - Black (LUXO)')
                    print('2 - Premium (CONFORTO)')
                    print('3 - Classic (ECONOMICO)')
                    print('4 - Outro')
                    classe = input('DIGITE A CLASSE DESEJADA: ')

                    if classe == '1':
                        print('\nMODELOS DISPONIVEIS DA CLASSE BLACK:')
                        print(f'1 - {carros[0]["black1"]}')
                        print(f'2 - {carros[0]["black2"]}')
                        print(f'3 - {carros[0]["black3"]}')
                        modelo = input('DIGITE O NUMERO DO MODELO DESEJADO: ')
                        if modelo == '1':
                            modelo = carros[0]["black1"]
                        elif modelo == '2':
                            modelo = carros[0]["black2"]
                        elif modelo == '3':
                            modelo = carros[0]["black3"]

                    elif classe == '2':
                        print('\nMODELOS DISPONIVEIS DA CLASSE PREMIUM:')
                        print(f'1 - {carros[0]["premium1"]}')
                        print(f'2 - {carros[0]["premium2"]}')
                        print(f'3 - {carros[0]["premium3"]}')
                        modelo = input('DIGITE O NUMERO DO MODELO DESEJADO: ')
                        if modelo == '1':
                            modelo = carros[0]["premium1"]
                        elif modelo == '2':
                            modelo = carros[0]["premium2"]
                        elif modelo == '3':
                            modelo = carros[0]["premium3"]

                    elif classe == '3':
                        print('\nMODELOS DISPONIVEIS DA CLASSE CLASSIC:')
                        print(f'1 - {carros[0]["classic1"]}')
                        print(f'2 - {carros[0]["classic2"]}')
                        print(f'3 - {carros[0]["classic3"]}')
                        modelo = input('DIGITE O NUMERO DO MODELO DESEJADO: ')
                        if modelo == '1':
                            modelo = carros[0]["classic1"]
                        elif modelo == '2':
                            modelo = carros[0]["classic2"]
                        elif modelo == '3':
                            modelo = carros[0]["classic3"]

                    elif classe == '4':
                        modelo = input('DIGITE O MODELO DO VEICULO: ')

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
                        'detalhe': detalhe,
                        'modelo': modelo,
                        'passageiros': []
                    })
                    print('CARONA CADASTRADA COM SUCESSO!')
                    print('              ')

                elif op2 == '2':
                    if len(usr_carona) == 0:
                        print('                                                       ')
                        print('-------------------------------------------------------')
                        print('--------- NENHUMA CARONA DISPONIVEL NO MOMENTO---------')
                        print('-------------------------------------------------------')
                        print('                                                       ')


                    else:
                        i = 1
                        qtd = 0
                        print('TODAS AS CARONAS DISPONÍVEIS:')
                        for carona in usr_carona:
                            if carona['nome'] == usuario_logado['nome']:
                                qtd = + 1
                                continue
                            if qtd == 0:
                                print(f"\nCARONA {i}:")
                                print(
                                    f"Motorista: {carona['nome']}  \n Local de Partida: {carona['local de partida']} \n Destino Final: {carona['destino final']} \n Data: {carona['dia']} / {carona['mes']} / {carona['ano']} \n Horário: {carona['horario']}:00 \n Vagas: {carona['vagas']} \n Valor por vaga: R${carona['valor por vaga']:.2f} \n Detalhe da viagem {carona['detalhe']} \n Modelo do carro {carona['modelo']}")
                                print('                                                       ')
                                i += 1

                            else:
                                print(f"\nCARONA {i}:")
                                print(
                                    f"Motorista: {carona['nome']} \n Local de Partida: {carona['local de partida']} \n Destino Final: {carona['destino final']} \n Data: {carona['dia']} / {carona['mes']} / {carona['ano']} \n Horário: {carona['horario']} \n Vagas: {carona['vagas']} \n Valor por vaga: R${carona['valor por vaga']:.2f} \n Detalhe da viagem {carona['detalhe']} \n Modelo do carro {carona['modelo']}")
                                print('                                                       ')
                                i += 1


                elif op2 == '3':
                    while True:
                        if len(usr_carona) > 1:
                            origem_busca = input('Digite a origem desejada: ')
                            destino_busca = input('Digite o destino desejado: ')

                            classe_modelo_de_carro = input('Deseja filtrar por classe do carro? (S/N): ').upper()
                            classe_filtro = None

                            if classe_modelo_de_carro == 'S':
                                print('\nESCOLHA A CLASSE DO VEICULO:')
                                print('1 - Black (Luxo)')
                                print('2 - Premium (Conforto)')
                                print('3 - Classic (Econômico)')
                                print('4 - Outro')
                                classe_opcao = input('DIGITE A CLASSE DESEJADA: ')

                                if classe_opcao == '1':
                                    classe_filtro = 'Black'
                                elif classe_opcao == '2':
                                    classe_filtro = 'Premium'
                                elif classe_opcao == '3':
                                    classe_filtro = 'Classic'
                                elif classe_opcao == '4':
                                    classe_filtro = 'Outro'

                            caronas_encontradas = False

                            print('\nRESULTADOS DA BUSCA:')
                            print('-------------------------------------------------------')
                            for carona in usr_carona:
                                if (origem_busca in carona['local de partida'] or destino_busca in carona[
                                    'destino final'] and carona['vagas'] > 0):
                                    print(
                                        f"Motorista: {carona['nome']}  \n Local de Partida: {carona['local de partida']} \n Destino Final: {carona['destino final']} \n Data: {carona['dia']} / {carona['mes']} / {carona['ano']} \n Horário: {carona['horario']}:00 \n Vagas: {carona['vagas']} \n Valor por vaga: R${carona['valor por vaga']:.2f} \n Detalhe da viagem {carona['detalhe']} \n Modelo do carro {carona['modelo']}")
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

                elif op2 == '4':
                    if len(usr_carona) == 0:
                        print('-------------------------------------------------------')
                        print('              NENHUMA CARONA DISPONÍVEL               ')
                        print('-------------------------------------------------------')
                    else:
                        while True:
                            i = 1
                            print('Caronas disponíveis:')
                            for carona in usr_carona:
                                if carona['vagas'] > 0:
                                    print(
                                        f"{i}. Motorista: {carona['nome']} - {carona['local de partida']} para {carona['destino final']} em {carona['dia']}/{carona['mes']}/{carona['ano']} às {carona['horario']}:00 \n Numero de vagas: {carona['vagas']} \n Detalhe da Viagem: {carona['detalhe']} Modelo:{carona['modelo']} ")
                                    i += 1
                                    print()
                            reserva = int(input('Escolha o número da carona que deseja reservar: (caso deseja voltar digite 0). '))

                            if reserva:
                                reserva -= 1
                                if 0 <= reserva < len(usr_carona):
                                    carona = usr_carona[reserva]
                                    if carona['vagas'] > 0:
                                        if usuario_logado['email'] in carona['passageiros']:
                                            print('Você já reservou uma vaga nesta carona!')
                                        elif usuario_logado['email'] == carona['email']:
                                            print('Você não pode reservar 1 vaga sendo o motorista')
                                        else:
                                            carona['vagas'] -= 1
                                            carona['passageiros'].append(usuario_logado['email'])
                                            print('Vaga reservada com sucesso!')
                                            break
                                    else:
                                        print('Não há vagas disponíveis nesta carona.')
                                else:
                                    print('Número de carona inválido!')
                            elif reserva == 0:
                                print('RETORNANDO PARA PAGINA INICIAL')
                                break
                            else:
                                print('Por favor, digite um número válido.')

                elif op2 == '5':
                    while True:
                        if len(usr_carona) == 0:
                            print('                                                       ')
                            print('-------------------------------------------------------')
                            print('--------- NENHUMA CARONA DISPONIVEL NO MOMENTO---------')
                            print('-------------------------------------------------------')
                            print('                                                       ')
                        else:
                            print('SUAS RESERVAS')
                            i = 1
                            reservas_carona = []
                            for carona in usr_carona:
                                if usuario_logado['email'] in carona['passageiros']:
                                    reservas_carona.append(carona)
                                    print(
                                        f'{i}. Motorista: {carona['nome']} - {carona['local de partida']} para {carona['destino final']} em {carona['dia']}/{carona['mes']}/{carona['ano']} às {carona['horario']}:00 \n Numero de vagas: {carona['vagas']} \n Detalhe da Viagem: {carona['detalhe']} Modelo:{carona['modelo']}')
                                    i += 1
                            if reservas_carona:
                                num_cancelar = int(input('Digite o numero da vaga que voce deseja cancelar: '))
                            else:
                                print('voce não possui caronas!')
                                break


                        if num_cancelar:
                            if 0 <= num_cancelar <= len(reservas_carona):
                                carona = reservas_carona[num_cancelar - 1]
                                carona['passageiros'].remove(usuario_logado['email'])
                                carona['vagas'] +=1
                                print('\nSua reserva foi cancelada com sucesso\n')
                                break


                elif op2 == '6':
                    print('                             ')
                    print('SAINDO DO MENU DE CARONAS ... ')
                    print('                             ')
                    op2 = '0'
                    usuario_logado = None
                    break
                else:
                    print('OPÇÃO INVALIDA!')

    elif op == '3':
        print('SAINDO DO SISTEMA ATE BREVE! ...')
    else:
        print('OPÇÃO INVALIDA')

