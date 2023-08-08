from account import CustomerAccount
from customer import CustomerDetails


def print_initial_menu() -> None:
    text = '''  
    ########### INITIAL MENU ###########
    (c) - Menu do cliente
    (a) - Acesse sua conta
    (q) - Sair                
    '''

    print (text)


def print_customer_menu() -> None:
    text = '''  
    ########### INITIAL MENU ###########
    (c) - Criar novo cliente
    (l) - Listar informação de um cliente
    (u) - Update nos campos de conta existente
    (a) - Criar conta e associar ao novo cliente
    (q) - Sair                
    '''

    print (text)


def print_account_menu() -> None:
    text = '''  
    ########### ACCOUNT MENU ###########
    (s) - Saque
    (d) - Deposito
    (e) - Extrato
    (q) - Sair                
    '''

    print (text)


def get_user_cpf() -> str:
    cpf_str = str(input("Entre com o seu cpf: "))
    cpf = ''.join(map(str,[int(i) for i in cpf_str if i.isdigit()]))
    return cpf


def get_user_data(get_cpf) -> (str, str, str, str):
    if get_cpf == True:
        cpf = get_user_cpf()
    else:
        cpf = None
    name = str(input("Entre com o seu nome: "))
    birthday = str(input("Entre com o dia do seu aniversário (DD/MM/YYYY): "))
    address = str(input("Entre com o seu endereço: "))
    return cpf, name, birthday, address


def customer_menu_control() -> None:
    while True:
        print_customer_menu()
        option = str(input("Digite sua opção: "))

        if (option == 'c'):
            cpf, name, birthday, address = get_user_data(True)
            customer = verify_customer_exist(cpf)
            if (customer != None):
                print(f'Cliente com o cpf {cpf} já está em nosso banco de dados')
                continue

            bank_customer_list.append(CustomerDetails(name=name, birthday=birthday, cpf=cpf, address=address))
            print(f"Cliente {name} adicionado com sucesso.")
            continue

        if (option == 'l'):
            cpf = get_user_cpf()
            custom0er = verify_customer_exist(cpf)
            if (customer == None):
                print(f'Cliente com o {cpf} não faz parte do nosso banco de dados')
                continue

            print(f" Nome: {customer.name} \n Aniversário: {customer.birthday} \n CPF: {customer.cpf} \n Endereço: {customer.address}")
            print("Accounts id: ")
            for a in bank_customer_account_association:
                if a["cpf"] == cpf:
                    acc = a["account_id"]
                    print (f"{acc}")
            continue

        if (option == 'u'):
            cpf = get_user_cpf()
            customer = verify_customer_exist(cpf)
            if (customer == None):
                print(f'Cliente com o {cpf} não faz parte do nosso banco de dados')
                continue
            
            c, name, birthday, address = get_user_data(False)
            customer.update_fields(name=name, birthday=birthday, address=address)
            continue

        if (option == 'a'):
            cpf = get_user_cpf()
            customer = verify_customer_exist(cpf)
            if (customer == None):
                print(f'Cliente com o {cpf} não faz parte do nosso banco de dados')
                continue

            initial_deposit = float(input("Entre com o valor do deposito inicial (R$): "))
            
            global next_account_id
            account = CustomerAccount(next_account_id, initial_deposit)
            next_account_id += 1

            bank_account_list.append(account)
            bank_customer_account_association.append({"cpf":customer.cpf, "account_id":account.account_id})
            continue

        if option == 'q':
            break


def account_menu_control() -> None:
    cpf = get_user_cpf()
    customer = verify_customer_exist(cpf)
    if (customer == None):
        print(f'Cliente com o {cpf} não faz parte do nosso banco de dados')
        return
    
    account_id = int(input("Entre com o numero da conta: "))
    account = verify_account_exist(account_id)
    if (account == None):
        print(f'Conta com o id {account_id} não faz parte do nosso banco de dados')
        return

    if verify_account_associtiation(cpf, account_id) == False:
        print(f'Cliente {customer.name} não possui conta com id {account_id}')
        return
    
    while True:
        print_account_menu()
        option = str(input("Digite sua opção: "))

        if option == 's':
            print(account.cash_withdraw(ammount=float(input("Entre com o valor: "))))
            continue
    
        if option == 'd':
            print(account.cash_deposit(float(input("Entre com o valor: "))))
            continue

        if option == 'e':
            account.show_bank_statment()
            continue
        
        if option == 'q':
            break


def verify_customer_exist(cpf: str) -> CustomerDetails:
    for cd in bank_customer_list:
        if (cd.cpf == cpf):
            return cd
        
    return None


def verify_account_exist(account_id: int) -> CustomerAccount:
    for ca in bank_account_list:
        if (ca.account_id == account_id):
            print(ca.account_id)
            return ca
        
    return None


def verify_account_associtiation(cpf: str, account_id: int) -> bool:
    for a in bank_customer_account_association:
        if (a["cpf"] == cpf and a["account_id"] == account_id):
            return True
        
    return False


bank_customer_list = []
bank_account_list = []
bank_customer_account_association = []
next_account_id = int(1)

bank_customer_list.append(CustomerDetails(name="Alu", birthday="01/10/1983", cpf="1234567890", address="Test"))

while True:
    print_initial_menu()
    option = str(input("Digite sua opção: "))

    if (option == 'c'):
        customer_menu_control()
        continue

    if (option == 'a'):
        account_menu_control()
        continue

    if (option == 'q'):
        break


print("Obrigado e volte sempre!")