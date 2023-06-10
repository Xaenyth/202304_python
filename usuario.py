class usuario:
    def __init__(self, name, last_name, email, balance_account):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.balance_account = balance_account
    def hacer_retiro(self,cantidad):
        if cantidad > self.balance_account:
            print("no hay saldo suficiente.")
        else:
            self.balance_account -=cantidad
            print(f"se retiraron ${cantidad}. nuevo saldo: ${self.balance_account}")

    def hacer_depocito(self, cantidad):
        self.balance_account += cantidad
        print(f"se han depositado ${cantidad}. saldo actural es: ${self.balance_account}")
    def ver_balance(self):
        return f"el balance de {self.name} es: ¨{self.balance_account}"

user1 = usuario("jose", "parraguez", "jose@gmail.com", 200)
user2 = usuario("alverto","parra","alverto@gmail.com", 500)
user3 = usuario("maria","figueroa","maria@gmail.com",300)

#usuario 1
usuario = user1
usuario.hacer_depocito(350)
usuario.hacer_depocito(230)
usuario.hacer_depocito(1200)
usuario.hacer_retiro(1500)
print(user1.ver_balance())
#usuario 2
usuario = user2
usuario.hacer_depocito(2000)
usuario.hacer_depocito(500)
usuario.hacer_retiro(1200)
usuario.hacer_retiro(500)
print(user2.ver_balance())
#usuario 3
usuario = user3
usuario.hacer_depocito(10000)
usuario.hacer_retiro(5000)
usuario.hacer_retiro(2500)
usuario.hacer_retiro(700)
print(user3.ver_balance())