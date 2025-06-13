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
    if '@' in email and '.com' in email and '$' not in email and '%' not in email and '&' not in email and '#' not in email and ' ' not in email and '/' not in email and '?' not in email:
        return True
    return False

def limpar_terminal():
    os.system('cls')