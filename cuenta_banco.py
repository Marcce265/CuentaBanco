class CuentaBanco:
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        # IMPORTANTE: Usamos __saldo para que sea privado (Encapsulamiento)
        self.__saldo = saldo_inicial

    def deposito_cuenta(self, monto: float):
        # Validación de tipo y monto positivo
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser numérico")
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        
        self.__saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")

    def retiro_cuenta(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente para el retiro")
        
        self.__saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")

    def transferencia_cuenta(self, monto: float, cuenta_destino):
        # Validar que la cuenta destino sea del tipo correcto
        if not isinstance(cuenta_destino, CuentaBanco):
            raise TypeError("La cuenta destino no es válida")
        
        # Lógica: Retirar de aquí y depositar allá
        self.retiro_cuenta(monto)
        cuenta_destino.deposito_cuenta(monto)
        print(f"Transferencia de {monto} a {cuenta_destino.titular} realizada.")

    def saldo_cuenta(self) -> float:
        return self.__saldo
    