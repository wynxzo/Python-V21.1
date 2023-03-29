class CuentaBancaria:
    cuentas=[]
    def __init__(self, tasa_interes, balance): 
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def depósito(self, amount):
        self.balance +- amount
        return self
    
    def retiro(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print(1000)
            self.balance -= 5
        return self
    
    def mostrar_info_cuenta(self):
        return (f"{self.balance}")
    
    def generar_interés(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interés)
        return self
    
    def imprime(self):
        print(f"{self.tasa_interes}  monto {self.balance}")
        return self

i1= CuentaBancaria (0.2,5000) 
    
i1.depósito(12)

i1.retiro(12)

i1.mostrar_info_cuenta()

i1.imprime()