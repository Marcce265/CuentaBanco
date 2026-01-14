class CuentaBanco:
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        """
        Constructor de la clase CuentaBanco.

        :param titular: Nombre del titular de la cuenta
        :param saldo_inicial: Saldo inicial de la cuenta (por defecto 0.0)
        """
        self.titular = titular
        self.saldo = saldo_inicial

    def deposito_cuenta(self, monto: float):
        if isinstance(monto, (int, float)) and monto > 0:
            self.saldo += monto
        else:
            raise ValueError("El monto a depositar debe ser un valor positivo.")

    def retiro_cuenta(self, monto: float):
        if isinstance(monto, (int, float)) and monto > 0:
            if monto <= self.saldo:
                self.saldo -= monto
            else:
                raise ValueError("Fondos insuficientes para realizar el retiro.")
        else:
            raise ValueError("El monto a retirar debe ser un valor positivo.")

    def transferencia_cuenta(self, monto: float, cuenta_destino):
        if not isinstance(cuenta_destino, CuentaBanco):
            raise ValueError("La cuenta destino no es válida.")
        if isinstance(monto, (int, float)) and monto > 0:
            if monto <= self.saldo:
                self.saldo -= monto
                cuenta_destino.saldo += monto
            else:
                raise ValueError("Fondos insuficientes para realizar la transferencia.")
        else:
            raise ValueError("El monto a transferir debe ser un valor positivo.")

    def saldo_cuenta(self) -> float:
        return self.saldo
