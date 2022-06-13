class CuentaBancaria:
    def __init__(self, tasa_interés, balance=0): 
        self.tasa_interés = tasa_interés
        self.balance =balance


    def depósito(self, monto):
        self.balance += monto  
        return self


    def retiro(self, monto):
        if monto > self.balance:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= monto+5
        else:
            self.balance -= monto
        return self


    def mostrar_info_cuenta(self):
        print(f"Balance ${self.balance}")
        return self


    def generar_interés(self):
        print (f"Con una tasa de interés de {self.tasa_interés}:")
        self.balance= self.balance + (self.tasa_interés)*(self.balance)
        self.mostrar_info_cuenta() 
        print("\t")
        return self



class Usuario:
    def __init__(self, name, last_name, age,tipocuenta):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.tipocuenta = tipocuenta
        if tipocuenta == "Cuenta Corriente":
            self.cuenta = CuentaBancaria(0.01,0)
        if tipocuenta == "Cuenta de ahorro":
            self.cuenta = CuentaBancaria(0.1,0) 
        if tipocuenta == "Cuenta Masterplop":
            self.cuenta= CuentaBancaria(0, 1000)


    def hacer_deposito(self,x):
        print(f"Usuario: {self.name} {self.last_name}. Tipo de cuenta: {self.tipocuenta}")
        print(f"Se han depositadado: ${x}")
        self.cuenta.depósito(x)
        self.cuenta.mostrar_info_cuenta() 
        self.cuenta.generar_interés()
        return self

    def hacer_retiro(self,x):
        print(f"Usuario: {self.name} {self.last_name}. Tipo de cuenta: {self.tipocuenta}")
        print(f"Se han retirado: ${x}")
        self.cuenta.retiro(x)
        self.cuenta.mostrar_info_cuenta() 
        self.cuenta.generar_interés()
        return self


guido = Usuario("Guido", "van Rossum", 25,"Cuenta de ahorro")
guido.hacer_deposito(10000).hacer_retiro(5000).hacer_deposito(50000)
guido= Usuario("guido", "van Rossum", 25,"Cuenta Corriente")
guido.hacer_deposito(50000).hacer_retiro(500)

monty = Usuario("Monty", "Python", 28, "Cuenta Corriente")
monty.hacer_deposito(2000)
monty = Usuario("Monty", "Python", 28, "Cuenta Masterplop")
monty.hacer_retiro(50)
