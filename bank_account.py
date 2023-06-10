class CuentaBancaria:
    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
    def deposito(self, amount):
        self.balance += amount
        return self
    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("saldo insuficiente para realizar retiro.")
        return self
    def mostrar_info_cuenta(self):
        print(f"cuentabancaria\ntasa de interes: {self.tasa_interes}%\nsaldo disponible: ${self.balance}")
        return self
    def generar_interes(self):
        interes_generado =self.balance * (self.tasa_interes/100)
        self.balance += interes_generado
        print(f"interes generado: ${interes_generado:.2f}")
        return self

cuenta1 = CuentaBancaria(0.07, 10000)
cuenta1.deposito(2000).deposito(1500).deposito(1000).retiro(5000).generar_interes().mostrar_info_cuenta()

cuenta2 = CuentaBancaria(0.04,3000)
cuenta2.deposito(5000).deposito(2000).retiro(1000).retiro(500).retiro(2000).retiro(4000).generar_interes().mostrar_info_cuenta()







