DAILY_LIMIT_CASH = 500
DAILY_LIMIT_CASH_WITHDRAW = 3

class CustomerAccount :    
    def __init__(self, account_id: int, initial_deposit: float) -> None:
        self.account_id = account_id
        self.cash_total = initial_deposit
        self.bank_statment = []
        self.daily_cash_withdraw = 0

    def cash_withdraw(self, *, ammount: float) -> str:
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

    def cash_deposit(self, ammount: float, /) -> str:
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


