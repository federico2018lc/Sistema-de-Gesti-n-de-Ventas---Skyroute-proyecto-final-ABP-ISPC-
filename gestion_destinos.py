import conectormysql  #módulo para obtener el conector y cursor de MySQL para poder hacer modificaciones en la base de datos skyroute

def gestionar_destinos():

    while True:
        print("\n")
        print("Gestionar Destino")
        print("1. Agregar nuevo Destino")
        print("2. Ver Destinos")
        print("3. Modificar Destino")
        print("4. Eliminar Destino")
        print("5. Atrás")
        
        opcion= input("Ingrese opción:")
        
        print(f"Seleccionó opción: {opcion}")
        
        conector, cursor = conectormysql.conectarDB() 
        #conector y cursor son los return de la funcion conectarDB definida en el modulo conectormysql.py
        #conector es la conexion a la base de datos y cursor ejecuta consultas SQL
        
        if opcion=="1": #agregar destino
            print("Agregar nuevo destino")
            print("Ingrese datos del destino elegido")
            
            # Ingreso de datos
            precio = input ("Ingrese el precio: ")
            ciudad = input ("Ingrese la ciudad: ")
            pais = input ( "Ingrese el pais: ")            
            try:
                # Consulta SQL para insertar
                query = """
                    INSERT INTO destinos (precio, pais, ciudad)
                    VALUES (%s, %s, %s)
                """
                # %s es un marcador de posición para los valores que se van a insertar
                # Los valores se pasan como una tupla al ejecutar la consulta
                
                cursor.execute(query, (precio, pais, ciudad)) # Ejecutar consulta con los valores ingresados
                conector.commit()# Commit para guardar los cambios en la base de datos
                
                print(f"Ha agregado el Destino {ciudad} - {pais}")
            except Exception as e:
                print("Error al agregar Destino:", e)
                
        # Si ocurre un error, se captura la excepción y se imprime un mensaje de error
        
        
        elif opcion=="2": #ver destinos
            print("Lista de Destinos disponibles de Skyroute")
            print("=========================================")
            cursor.execute("SELECT * FROM destinos")#consulta SQL para seleccionar todos los destinos
            destinos = cursor.fetchall()   #fetchall crea una lista de destinos (lista de tuplas)

            if destinos:
                for x in destinos:
                    print(f"Código de Destino:{x[0]}     Precio:{x[1]}     Cuidad: {x[2]}    Pais: {x[3]}")
                    print(".....................................................................")
            else:
                print("No hay destinos registrados")

        elif opcion=="3": #modifcar
            print("Modificar Destino")
            codigo_destino = input("Ingrese el codigo del destino que desea modificar: ")
            cursor.execute("SELECT * FROM destinos WHERE codigo_destino = %s", (codigo_destino,)) #Consulta SQL para seleccionar el cliente por cuit
            # %s es un marcador de posición para el valor del codigo destino
            destino = cursor.fetchone()    #crea una tupla con los datos del destino.

            if destino:
                print("Datos actuales del Destino:",destino)   #imprimo tupla destino
                precio=input("Ingrese nuevo precio del destino: ")
                ciudad=input("Ingrese nueva ciudad del destino: ")
                pais=input("Ingrese el nuevo país del destino:") 

                cursor.execute("""
                UPDATE destinos
                SET precio = %s, ciudad =%s, pais =%s 
                WHERE codigo_destino = %s""", (precio, ciudad, pais, codigo_destino))
                conector.commit() # Commit para guardar los cambios en la base de datos
                print("Destino modificado")
            else:
                print("No se encontró un destino con ese código")

        elif opcion=="4": #eliminar destino
            codigo_destino=input("ingresar código del destino a  eliminar:") 
            cursor.execute("SELECT * FROM destinos WHERE codigo_destino = %s", (codigo_destino,))
            destino = cursor.fetchone() #fetchone crea una tupla con los datos del destino

            if destino:
                print("¿Está seguro que desea eliminar el destino:", destino, "?")
                print("Esta acción no se puede deshacer ⚠️")
                respuesta = input("Ingrese 'si' para confirmar o 'no' para cancelar: ")
                if respuesta.lower() == 'si':
                    sql = "DELETE FROM destinos WHERE codigo_destino = %s "
                    cursor.execute(sql,(codigo_destino,)) 
                    conector.commit()
                    print(f"eliminó el destino: {destino}")
                else:
                    print("Eliminación cancelada.")
            else:
                print("No se encontro destino con ese codigo")

        elif opcion=="5":
            break
        else:
            print("Opción no valida.")
        print("=====================")
    cursor.close()
    conector.close()
