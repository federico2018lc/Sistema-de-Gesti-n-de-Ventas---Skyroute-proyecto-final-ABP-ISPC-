import conectormysql  # módulo para obtener el conector y cursor de MySQL

def gestionar_clientes():
    def validar_cuit(cuit):
        return cuit.isdigit() and len(cuit) == 11

    while True:
        print("Gestionar clientes")
        print("1. Agregar nuevo cliente")
        print("2. Ver clientes")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Volver al menú principal")
        opcion = input("Ingrese opción:")
        print(f"Seleccionó opción: {opcion}")
        conector, cursor = conectormysql.conectarDB()

        if opcion == "1":  # Agregar cliente
            print("Agregar nuevo cliente")
            print("Ingrese los datos del cliente")

            while True:
                cuit = input("Cuit (11 dígitos): ")
                if validar_cuit(cuit):
                    break
                print("CUIT inválido. Debe tener exactamente 11 dígitos numéricos.")

            razon_social = input("Razón Social: ")
            mail = input("Ingrese mail: ")

            try:
                query = """
                    INSERT INTO clientes (cuit, razon_social , mail)
                    VALUES (%s, %s, %s)
                """
                cursor.execute(query, (cuit, razon_social, mail))
                conector.commit()
                print(f"Ha agregado al cliente {razon_social} CUIT: {cuit}")
            except Exception as e:
                print("Error al agregar cliente:", e)
        #Acá pueden ocurrir varios tipos de errores al ingresar datos por teclado, como por ejemplo:
        # - Error de duplicado de clave primaria (si el cuit ya existe) 
        # - Error de tipo de dato (si se ingresa letras en lugar de números en el cuit)

        elif opcion == "2":  # Ver clientes
            print("Lista de Clientes de skyroute")
            print("================================")
            cursor.execute("SELECT * FROM clientes")
            clientes = cursor.fetchall()  #crea una lista de tuplas con los datos del cliente

            if clientes:
                for x in clientes:
                    print(f"CUIT: {x[0]}  |   Razón Social: {x[1]}  |   Mail: {x[2]}")
                    print(".....................................................................")
            else:
                print("No hay clientes registrados")

        elif opcion == "3":  # Modificar cliente
            print("Modificar cliente")
            while True:
                cuit = input("Ingrese el CUIT del cliente que desea modificar (11 dígitos): ")
                if validar_cuit(cuit):
                    break
                print("CUIT inválido. Debe tener exactamente 11 dígitos numéricos.")

            cursor.execute("SELECT * FROM clientes WHERE cuit = %s", (cuit,))
            cliente = cursor.fetchone() #crea una tupla con los datos del cliente

            if cliente:
                print("Datos actuales del cliente:", cliente)
                razon_social = input("Ingrese la nueva razón social: ")
                mail = input("Ingrese el nuevo mail:")

                cursor.execute("""
                    UPDATE clientes
                    SET razon_social = %s, mail = %s 
                    WHERE cuit = %s""", (razon_social, mail, cuit))
                conector.commit()
                print("Cliente modificado")
            else:
                print("No se encontró cliente con ese CUIT")

        elif opcion == "4":  # Eliminar cliente
            while True:
                cuit = input("Ingrese el CUIT del cliente que desea eliminar (11 dígitos): ")
                if validar_cuit(cuit):
                    break
                print("CUIT inválido. Debe tener exactamente 11 dígitos numéricos.")

            cursor.execute("SELECT * FROM clientes WHERE cuit = %s", (cuit,))
            cliente = cursor.fetchone()

            if cliente:
                print("¿Está seguro que desea eliminar los datos del cliente:")
                print(f"CUIT: {cliente[0]}  |  Razón Social: {cliente[1]}  |  Mail: {cliente[2]}?")
                print("Esta acción no se puede deshacer ⚠️")
                respuesta = input("Ingrese 'si' para confirmar o 'no' para cancelar: ")
                if respuesta.lower() == 'si':
                    cursor.execute("DELETE FROM clientes WHERE cuit = %s", (cuit,))
                    conector.commit()
                    print(f"Eliminó el cliente CUIT: {cuit}")
                else:
                    print("Eliminación cancelada.")
            else:
                print("No se encontró cliente con ese CUIT")

        elif opcion == "5":
            break
        else:
            print("Opción no válida.")
        
        print("================================")
        cursor.close()
        conector.close()
