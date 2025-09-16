import gestion_clientes
import gestion_destinos
import gestion_ventas
import boton_de_arrepentimiento
#menú principal
while True:

    print("==============================")
    print("Bienvenido a skyroute")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Boton de Arrepentimiento")
    print("5. Acerca del Sistema")
    print("6. SALIR")
    print("==============================")
    opcion = input("Ingrese una opción: ")
    print(f"Seleccionó opción: {opcion}")
    
    if opcion == "1":
        gestion_clientes.gestionar_clientes()  #cuando usamos alguna funcion de algun módulo primero nombremodulo.nombrefuncion()
    elif opcion == "2":
        gestion_destinos.gestionar_destinos()
    elif opcion == "3":
        gestion_ventas.gestionar_ventas()
    elif opcion == "4":
        boton_de_arrepentimiento.boton_arrepentimiento()
    elif opcion == "5":
        print("Acerca del Sistema:")
        print("Sistema de Gestión de Ventas de Skyroute")
        print("Desarrollado por Grupo PY S.R.L.")
        print("Este sistema permite gestionar clientes, destinos y ventas de manera eficiente.")
        print("Este software se encuentra protegido por la Ley de Propiedad Intelectual N.° 11.723 de la República Argentina.")
        print("Este sistema almacena información personal en cumplimiento con la Ley N.° 25.326 de Protección de los Datos Personales.")
    elif opcion == "6":
        print("Seleccionó SALIR. \nGracias por usar Sistema de Gestión de Ventas de Skyroute. Hasta luego.")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
