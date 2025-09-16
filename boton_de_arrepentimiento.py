import conectormysql
from datetime import datetime, timedelta


def boton_arrepentimiento():
    print("\n=== BOTÓN DE ARREPENTIMIENTO ===")
    codigo_venta = input("Ingrese el código de la venta que desea anular: ")

    conector, cursor = conectormysql.conectarDB()

    # Buscar la venta
    cursor.execute(
        "SELECT codigo_venta, fecha_de_venta, hora_de_venta, estado FROM ventas WHERE codigo_venta = %s",
        (codigo_venta,),
    )
    venta = cursor.fetchone()

    if not venta:
        print("❌ No se encontró ninguna venta con ese código.")
    else:
        estado_actual = venta[3]
        if estado_actual == "Anulada":
            print("⚠️ La venta ya fue anulada anteriormente.")
        else:
            # Construir datetime completo desde fecha y hora de venta
            fecha_hora_str = f"{venta[1]} {venta[2]}"
            fecha_hora_venta = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M:%S")
            ahora = datetime.now()

            # Calcular si pasaron más de 5 minutos
            if ahora - fecha_hora_venta <= timedelta(seconds=20):#usamos una escala en la que 20 segundos equivale a 60 dias
                # Actualizar estado de la venta
                cursor.execute(
                    "UPDATE ventas SET estado = 'Anulada' WHERE codigo_venta = %s",
                    (codigo_venta,),
                )
                conector.commit()
                print(
                    "✅ Venta anulada correctamente dentro del plazo de arrepentimiento."
                )
            else:
                print("⏱️ El plazo de 60 días para anular la venta ha expirado.")

    cursor.close()
    conector.close()
