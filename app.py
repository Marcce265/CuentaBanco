from cuenta_banco import CuentaBanco

def mostrar_menu():
    print("\n--- MENÚ CAJERO CUENTA BANCO ---")
    print("1. Depósito")
    print("2. Retiro")
    print("3. Transferencia")
    print("4. Consulta de saldo")
    print("5. Salir")
    return input("Seleccione una opción: ")

def main():
    # Creamos las cuentas iniciales (asegúrate que coincidan con tu constructor en CuentaBanco)
    cuenta_origen = CuentaBanco(1000.0)
    cuenta_destino = CuentaBanco(500.0)

    while True:
        opcion = mostrar_menu()

        try:
            if opcion == "1":
                monto = float(input("Ingrese el monto a depositar: "))
                cuenta_origen.deposito_cuenta(monto)
            
            elif opcion == "2":
                monto = float(input("Ingrese el monto a retirar: "))
                cuenta_origen.retiro_cuenta(monto)
            
            elif opcion == "3":
                monto = float(input("Ingrese el monto a transferir a la cuenta destino: "))
                cuenta_origen.transferencia_cuenta(monto, cuenta_destino)
            
            elif opcion == "4":
                print(f"Su saldo actual es: {cuenta_origen.saldo_cuenta()}")
            
            elif opcion == "5":
                print("Saliendo del sistema... ¡Gracias!")
                break
            
            else:
                print("Opción no válida, intente de nuevo.")

        except (ValueError, TypeError) as e:
            # Capturamos los errores que programamos en la clase CuentaBanco
            print(f"⚠️ ERROR: {e}")

if __name__ == "__main__":
    main()