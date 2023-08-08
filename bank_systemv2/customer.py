import re

class CustomerDetails:
    def __init__(self, name, birthday, cpf, address) -> None:
        self.name = name

        if self.check_birthday_format (birthday) == True:
            self.birthday = birthday
        else:
            print(f"Dia do aniversário {birthday} Está no formato errado. Esperamos DD/MM/YYYY. \nConta será criada, mas com necessidade de update futuro nesse campo")

        self.cpf = ''.join(map(str,[int(i) for i in cpf if i.isdigit()]))
        print(self.cpf)
        self.address = address

    def check_birthday_format (self, birthday) -> bool:
        pattern_str = r'^\d{2}/\d{2}/\d{4}$'
        return True if re.match(pattern_str, birthday) else False
        
    def update_fields(self, name=None, birthday=None, cpf=None, address=None) -> None:
        if (name != None):
            self.name = name
            print(f"Name update")
        
        if (birthday != None):
            if self.check_birthday_format(birthday) == True:
                self.birthday = birthday
                print(f"Birthday update")
            else:
                print(f"Dia do aniversário {birthday} Está no formato errado. Esperamos DD/MM/YYYY") 
        
        if (cpf != None):
            self.cpf = str([int(i) for i in cpf.split() if i.isdigit()])
            print(f"CPF update")

        if (address != None):
            self.address = address
            print(f"Adress update")
