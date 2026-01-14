from cuenta_banco import CuentaBanco

def mostrar_menu():
    """Imprime las opciones disponibles en consola."""
    print("\n" + "="*30)
    print("      CAJERO AUTOMÁTICO")
    print("="*30)
    print("1. Depósito")
    print("2. Retiro")
    print("3. Transferencia")
    print("4. Consulta de saldo")
    print("5. Salir")
    return input("Seleccione una opción (1-5): ")

def main():
    # Instanciamos dos cuentas para poder probar transferencias entre ellas
    cuenta_kevin = CuentaBanco("Kevin", 1000.0)
    cuenta_destino = CuentaBanco("Juan Perez", 500.0)

    while True:
        opcion = mostrar_menu()

        try:
            if opcion == "1":
                monto = float(input("Ingrese monto a DEPOSITAR: "))
                cuenta_kevin.deposito_cuenta(monto)
            
            elif opcion == "2":
                monto = float(input("Ingrese monto a RETIRAR: "))
                cuenta_kevin.retiro_cuenta(monto)
            
            elif opcion == "3":
                print(f"Destinatario actual: {cuenta_destino.titular}")
                monto = float(input("Ingrese monto a TRANSFERIR: "))
                cuenta_kevin.transferencia_cuenta(monto, cuenta_destino)
            
            elif opcion == "4":
                saldo = cuenta_kevin.saldo_cuenta()
                print(f" Saldo actual de {cuenta_kevin.titular}: S/. {saldo:.2f}")
            
            elif opcion == "5":
                print("¡Gracias por usar nuestro sistema bancario! 👋")
                break
            
            else:
                print(" Opción inválida. Por favor, marque del 1 al 5.")

        except ValueError as e:
            # Captura errores de conversión (ej. escribir letras en vez de números)
            # y errores lanzados manualmente con 'raise ValueError'
            print(f" ERROR DE DATO: {e}")
        except TypeError as e:
            # Captura errores cuando el tipo de objeto no es el esperado
            print(f" ERROR DE TIPO: {e}")
        except Exception as e:
            # Captura cualquier otro error inesperado para que el programa no colapse
            print(f" OCURRIÓ UN ERROR INESPERADO: {e}")

if __name__ == "__main__":
    main()