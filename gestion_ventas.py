import conectormysql
import datetime as datatime

def gestionar_ventas():

    while True:
        print("Bienvenido a la gestión de ventas")
        print("1. Registrar una nueva venta")
        print("2. Consultar ventas")
        print("3. Anular una venta")
        print("4. Volver al menú principal")
    


        opcion = input("Ingrese una opción: ")
        conector, cursor = conectormysql.conectarDB() 

        if opcion == "1":
            print("Registrar una nueva venta")
            codigo_destino = input("Ingrese el codigo destino: ")
            cuit = input("Ingrese el cuit del cliente: ")
            fecha_de_viaje = input("(ingresar cantidad de dias (Ingrese la fecha de viaje (DD-MM-YYYY):) ")
            
            try:
                fecha_de_venta = datatime.datetime.now().strftime("%Y-%m-%d")
                print(f"Fecha de venta: {fecha_de_venta}")
                hora_de_venta = datatime.datetime.now().strftime("%H:%M:%S")
                print(f"Hora de venta: {hora_de_venta}")
                query = """
                        INSERT INTO ventas (codigo_destino, cuit, fecha_de_venta, hora_de_venta, fecha_de_viaje)
                        VALUES (%s, %s, %s, %s, %s)
                    """
                cursor.execute(query, (codigo_destino, cuit, fecha_de_venta, hora_de_venta, fecha_de_viaje)) 
                conector.commit()
                print(f"Venta registrada correctamente")

                    
            except Exception as e:
                print("Error al agregar Venta:", e)
        elif opcion == "2":
            print("Consultar ventas:")
            try:
                query = "SELECT * FROM ventas"
                cursor.execute(query)
                ventas = cursor.fetchall()
                if ventas:
                    for venta in ventas:
                        
                        print(f"Código Venta:{venta[0]}         Fecha de Venta:{venta[3]}       Hora de Venta: {venta[4]}")
                        print(f"Código de destino:{venta[1]}                    Cuit:{venta[2]}")  
                        print(f"Fecha de Viaje:{venta[5]}                       Estado:{venta[6]}")
                        print("................................................")
                else:
                    print("No hay ventas registradas.")
            except Exception as e:
                print("Error al consultar ventas:", e)
        elif opcion == "3":
            print("Anular una venta")
            print("Opción para anular ventas fuera del periodo de arrepentimiento")
            codigo_venta = input("Ingrese el código de la venta a anular: ")
            try:
                query = "UPDATE ventas SET estado='ANULADA' WHERE codigo_venta=%s"
                cursor.execute(query, (codigo_venta,))
                conector.commit()
                if cursor.rowcount > 0:
                    print(f"Venta {codigo_venta} anulada correctamente.")
                else:
                    print(f"No se encontró la venta con código {codigo_venta}.")
            except Exception as e:
                print("Error al anular la venta:", e)
        elif opcion == "4":
            print("Saliendo de la gestión de ventas.")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
    cursor.close()
    conector.close()

#gestionar_ventas()
