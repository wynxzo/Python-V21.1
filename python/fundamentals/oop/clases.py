class Usuario:  
    name_bank = "banco estado"    
    def __init__(self,name, email_address ) -> None:
        self.name = name
        self.email = email_address
        self.balance_cuenta = 0
    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
        return self
    def hacer_retiro(self, other_user):
        self.balance_cuenta -= other_user
        return self
    def imprime(self): 
        print(f"el usuario {self.name} el monto dela cuenta {self.balance_cuenta}")
        return self

    
    def transferencia(self,amount, user ):
        self.balance_cuenta -= amount
        user.balance_cuenta += amount
        self.imprime()
        user.imprime()
        return self
    



name ='ysi'
email = 'isi.poblete@gmail.com'
guido = Usuario(name,email)
name = 'kamila'
email = 'kamila.cas@gmail.com'
monty = Usuario(name,email)
guido.hacer_deposito(950).hacer_deposito(950).hacer_deposito(950).hacer_deposito(950)
guido.imprime()
monty.imprime()
guido.transferencia(950,monty)
'''
print(f" 1 {guido.name} ")  # salida: Michael
print(f" 2 {guido.email} ")
print(f" 3 {monty.name} ")  # salida: Michael
print(f" 4 {monty.email} ")

guido.name = "Guido"
print(guido.name) # salida: Guido
monty.name = "Monty"
print(monty.name) # salida: Monty
'''
