import os


def linhas():
    print('-' * 30)


def menu_principal(menu):
    linhas()
    print('-'*15, menu, '-'*15)
    print('-'*15, 'BLABLACA', '-'*15)
    linhas()
    print('1-CADASTRA USUARIO ')
    print('2-LOGIN')
    print('3-SAIR\n')
    linhas()
    linhas()


def verificar_email_exist(email, usr):
    for usuario in usr:
        if usuario['email'] == email:
            return False
    return True


def requisito_email(email):
    naopode = ['$', '%', '&', '#', ' ', '/', '?']
    if '@' not in email or not email.endswith('.com'):
        return False
    for caracteres in naopode:
        if caracteres in email:
            return False
    return True

def verificar_data(ano, mes, dia):
    if not 2025 <= ano <= 3000:
        return False

    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= dia <= 31

    if mes in [4, 6, 9, 11]:
        return 1 <= dia <= 30

    if mes == 2:
        bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
        return 1 <= dia <= (29 if bissexto else 28)

    return False

def verificar_horario(horario):
    if ':' in horario:
        divisao = horario.split(':')
        if len(divisao) == 2 and divisao[0] and divisao[1]:
            horas = int(divisao[0])
            minutos = int(divisao[1])
            if 0 <= horas < 24 and 0 <= minutos < 60:
                return True
    return False

def classe_carros():
    print('\nESCOLHA A CLASSE DO VEICULO:')
    print('1 - Black (LUXO)')
    print('2 - Premium (CONFORTO)')
    print('3 - Classic (ECONOMICO)')
    print('4 - Outro')

def carros_black(carros):
    print('\nMODELOS DISPONIVEIS DA CLASSE BLACK:')
    print(f'1 - {carros[0]["black1"]}')
    print(f'2 - {carros[0]["black2"]}')
    print(f'3 - {carros[0]["black3"]}')

def carros_premium(carros):
    print('\nMODELOS DISPONIVEIS DA CLASSE PREMIUM:')
    print(f'1 - {carros[0]["premium1"]}')
    print(f'2 - {carros[0]["premium2"]}')
    print(f'3 - {carros[0]["premium3"]}')

def carros_classic(carros):
    print('\nMODELOS DISPONIVEIS DA CLASSE CLASSIC:')
    print(f'1 - {carros[0]["classic1"]}')
    print(f'2 - {carros[0]["classic2"]}')
    print(f'3 - {carros[0]["classic3"]}')



def caronas_disponioveis(carona, i):
    print(f"\nCARONA {i}:")
    print(
        f"Motorista: {carona['nome']}  "
        f"\n Local de Partida: {carona['local de partida']} "
        f"\n Destino Final: {carona['destino final']} "
        f"\n Data: {carona['dia']} / {carona['mes']} / {carona['ano']} "
        f"\n Horário: {carona['horario']}:00 \n Vagas: {carona['vagas']} "
        f"\n Valor por vaga: R${carona['valor por vaga']:.2f} "
        f"\n Detalhe da viagem:  {carona['detalhe']} "
        f"\n Modelo do carro: {carona['modelo']}")
    print('                                                       ')

def continuar():
    kk = input('Para voltar pressione ENTER')


def falta_carona():
    print('                                                       ')
    print('-------------------------------------------------------')
    print('--------- NENHUMA CARONA CADASTRADA--------------------')
    print('-------------------------------------------------------')
    print('                                                       ')


def limpar_terminal():
    os.system('cls')