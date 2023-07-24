DAILY_LIMIT_CASH = 500
DAILY_LIMIT_CASH_WITHDRAW = 3

class CustomerAccount :
    bank_statment = []
    daily_cash_withdraw = 0
    cash_total = 0
    
    def __init__(self, customer_name, account_id, initial_deposit: float) -> None:
        self.customer_name = customer_name
        self.account_id = account_id
        self.cash_total = initial_deposit

    def cash_withdraw(self, ammount: float) -> str:
        if ammount > DAILY_LIMIT_CASH:
            return f"Quantidade requerida excede o limite R$ 500"
        
        if self.daily_cash_withdraw >= DAILY_LIMIT_CASH_WITHDRAW:
            return f"Quantidade de saques permitida no dia excedida"
        
        if self.cash_total < ammount:
            return f"Não é possivel sacar {ammount:>.2f}. Saldo insuficiente"

        self.daily_cash_withdraw += 1
        self.cash_total -= ammount
        self.add_bank_statement(f"Saque:      R$ {ammount:>8.2f}   -   Total: R$ {self.cash_total:.2f}")
        return (f"Saque realizado de R$ {ammount:.2f} com sucesso")

    def cash_deposit(self, ammount: float) -> str:
        self.cash_total += + ammount
        self.add_bank_statement(f"Deposito:   R$ {ammount:>8.2f}   -   Total: R$ {self.cash_total:.2f}")
        return (f"Deposito realizado de R$ {ammount:.2f} com sucesso")


    def show_bank_statment(self) -> None:
        if len(self.bank_statment) == 0:
            print(f"Não foram realizados operações na conta {self.account_id}")

        for s in self.bank_statment:
            print(s)
        
        print (f"\nTotal disponivel em conta: R$ {self.cash_total:.2f}")

    def add_bank_statement(self, text: str) -> None:
        self.bank_statment.append(text)


def print_menu() -> None:
    text = '''  
    ########### MENU ###########
    (s) - Saque
    (d) - Deposito
    (e) - Extrato
    (q) - Sair                
    '''

    print (text)


customer = CustomerAccount("John Doe", "0001", 1500)
print(f"Bem ao Banco do Zyzy Mr. {customer.customer_name}")

while True:
    print_menu()
    option = str(input("Digite sua opção: "))

    if option == 's':
        print(customer.cash_withdraw(float(input("Entre com o valor: "))))
        continue
    
    if option == 'd':
        print(customer.cash_deposit(float(input("Entre com o valor: "))))
        continue

    if option == 'e':
        customer.show_bank_statment()
        continue
    
    if option == 'q':
        break

print("Obrigado e volte sempre!")

