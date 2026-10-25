import json

def Cajero_Existe(usuario_tarjeta, usuarios):
    for indice in range(len(usuarios["usuarios"])):
        if(usuario_tarjeta == usuarios["usuarios"][indice]["numero_tarjeta"]):
            return indice

    return -1
def Cajero_Datos(usuario_indice, usuarios):
    print("Usuario/a: ", usuarios["usuarios"][usuario_indice]["nombre"])
    print("Saldo disponible: $", usuarios["usuarios"][usuario_indice]["saldo"])


def Usuarios_Retiro(usuario_indice, usuarios, efectivo_disponible):
    contador = 1

    while(contador != 3):

        print("Usuario/a: ", usuarios["usuarios"][usuario_indice]["nombre"])
        print("Saldo disponible: $", usuarios["usuarios"][usuario_indice]["saldo"])

        cantidad_retiro = float(input("\nIngrese la cantidad a retirar \n\n>> "))

        if(0 < cantidad_retiro and cantidad_retiro <= efectivo_disponible):
            usuarios["usuarios"][usuario_indice]["saldo"] -= cantidad_retiro
            return cantidad_retiro
        else:
            print("Cantidad invalida! Debe ser entre $0 y $", efectivo_disponible)
            contador += 1
        
    print("Usted ha superado el limite de intentos")
    return 0

def Usuarios_Depositos(usuario_indice, usuarios):
    contador = 1

    while(contador != 3):

        print("Usuario/a: ", usuarios["usuarios"][usuario_indice]["nombre"])
        print("Saldo disponible: $", usuarios["usuarios"][usuario_indice]["saldo"])

        cantidad_deposito = float(input("Ingrese la cantidad a depositar\n\n>> "))

        if(0 < cantidad_deposito and cantidad_deposito < 10000):
            usuarios["usuarios"][usuario_indice]["saldo"] += cantidad_deposito
            return cantidad_deposito
        else:
            print("La cantidad debe estar entre $0 y $10,000")
            contador += 1

    print("Usted ha superado el limite de intentos")
    return 0

def Usuarios_Transferencia(usuario_indice, usuarios):
    contador = 1

    while(contador != 3):

        print("Usuario/a: ", usuarios["usuarios"][usuario_indice]["nombre"])
        print("Saldo disponible: $", usuarios["usuarios"][usuario_indice]["saldo"])

        usuario_transferencia = input("Ingrese la cuenta destino\n\n>> ")

        if(Cajero_Existe(usuario_transferencia, usuarios) != -1):
            contador = 1

            while(contador != 3):
                cantidad_transferencia = float(input("Ingrese la cantidad a depositar\n\n>> "))

                if(cantidad_transferencia > 0 and cantidad_transferencia <= float(usuarios["usuarios"][usuario_indice]["saldo"])):
                    
                    usuarios["usuarios"][usuario_indice]["saldo"] -= cantidad_transferencia
                    usuarios["usuarios"][usuario_transferencia]["saldo"] += cantidad_transferencia

                    print("Transferencia exitosa!")
                    print("El/la señor/a: ", usuarios["usuario"][usuario_indice]["nombre"])
                    print("Ha transferido $", str(cantidad_transferencia), "al usuario: ", usuarios["usuario"][usuario_transferencia]["nombre"])

                    return 0
                else:
                    print("La cantidad es menor a 0 o supera su saldo actual")
                    contador += 1
        else:
            print("Numero de cuenta invalido.")
            contador += 1

        print("Usted ha superado el limite de intentos!")
        return -1
                    
def Usuarios_NuevoNIP(usuario_indice, usuarios):
    contador = 1

    while(contador != 3):
        usuario_nip = input("Ingrese su nip\n>> ")

        if(usuario_nip == usuarios["usuarios"][usuario_indice]["nip"]):
            contador = 1

            while(contador != 3):
                nuevo_nip = input("Ingrese el nuevo NIP: ")

                if(len(nuevo_nip) == 4):

                    usuarios["usuarios"][usuario_indice]["nip"] = nuevo_nip
                    print("El nip ha sido cambiado exitosamente")
                    
                    return 0
                else:
                    print("El nuevo nip debe ser de cuatro caracteres [XXXX]")
                    contador += 1
        else:
            print("NIP incorrecto.")
            contador += 1

    print("Usted supero el limite de intentos")
    return -1


if __name__ == "__main__":

    sesion_operacion = 0
    sesion_identificador = 0
    sesion_contador = 1
    sesion_efectivo = 200000

    with open("Usuarios.json", "r") as base_usuarios:
        usuarios = json.load(base_usuarios)

    print("======================= Cajero Automatico =======================")
    sesion_tarjeta = input("Ingrese el numero de tarjeta\n\n>> ")
    sesion_identificador = Cajero_Existe(sesion_tarjeta, usuarios)

    while(sesion_identificador == -1):
        print("Numero de tarjeta invalido")

        sesion_tarjeta = input("Ingrese el numero de tarjeta\n\n>> ")
        sesion_identificador = Cajero_Existe(sesion_tarjeta, usuarios)


    while(sesion_operacion != 6):
        print("======================= Seleccione =======================")
        
        print("Numero de tarjeta: ", usuarios["usuarios"][sesion_identificador]["numero_tarjeta"])
        print("Usuario: ", usuarios["usuarios"][sesion_identificador]["nombre"], "\n")
        
        print("1. Consultar Saldo")
        print("2. Retiro de efectivo")
        print("3. Deposito")
        print("4. Transferencia")
        print("5. Cambio de NIP")
        print("6. Cerrar sesion")

        sesion_operacion = int(input(">> "))

        if sesion_operacion == 1:
            Cajero_Datos(sesion_identificador, usuarios)
        elif sesion_operacion == 2:
            sesion_efectivo -= Usuarios_Retiro(sesion_identificador, usuarios, sesion_efectivo)
        elif sesion_operacion == 3:
            Usuarios_Depositos(sesion_identificador, usuarios)
        elif sesion_operacion == 4:
            Usuarios_Transferencia(sesion_identificador, usuarios)
        elif sesion_operacion == 5:
            Usuarios_NuevoNIP(sesion_identificador, usuarios)
        elif sesion_operacion == 6:
            print("Muchas gracias por su preferencia")

        print("--- click para continuar ---")
        input()

    with open("Usuarios.json", "w") as base_usuarios:
        json.dump(usuarios, base_usuarios, indent=4)