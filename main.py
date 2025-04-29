tem_email= ['@' '.com']
naotem_email = ['$', '%', '&','#',' ']
usr = []
senha = []

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

            if '@' in email and '.com' in email and '$' not in email and '%' not in email and '&' not in email and '#' not in email and ' ' not in email :
                usr.append({
                    'nome': nome,
                    'email': email,
                    'senha': senha
                }
                )
                print('Usuario cadastrado com sucesso')
                break
            else:
                print('email invalido por favor digite novamente email e senha para validação')
                continue