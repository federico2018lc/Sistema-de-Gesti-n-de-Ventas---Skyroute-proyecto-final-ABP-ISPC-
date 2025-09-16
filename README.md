# Sistema-de-Gesti-n-de-Ventas---Skyroute-proyecto-final-ABP-ISPC-
Proyecto educatico hecho en grupo en el primer semetres 2024
# ISPC-Modulo-Programador
# Sistema de Gestión de Ventas - Skyroute
Este proyecto fue desarrollado como parte de la carrera "Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial" en el ISPC.

El sistema permite gestionar clientes, destinos y ventas de una agencia de viajes llamada Skyroute, con conexión a una base de datos MySQL.

# Funcionalidades principales
* *Gestión de clientes*: alta, modificación, consulta y baja de clientes.
* *Gestión de destinos*: creación, modificación, listado y eliminación de destinos turísticos.
* *Gestión de ventas*: registro de ventas, consulta y anulación.
* *Botón de arrepentimiento*: permite anular una venta dentro de los primeros 5 minutos.

# Tecnologías utilizadas
* Python 3
* MySQL
* Visual Studio Code

# Estructura del sistema
* menu.py: menú principal del sistema.
* conectormysql.py: gestiona la conexión con la base de datos.
* gestion_clientes.py: módulo de operaciones sobre clientes.
* gestion_destinos.py: módulo de operaciones sobre destinos.
* gestion_ventas.py: módulo de operaciones sobre ventas.
* boton_de_arrepentimiento.py: módulo para anulación reciente de ventas.

# Cómo ejecutar
1. Crear la base de datos skyroute en MySQL con el archivo DB_skyroute.sql.
2. Editar conectormysql.py y completar usuario y contraseña local.
3. Ejecutar menu.py desde Visual Studio Code o terminal.

# Créditos
Proyecto realizado por Dante Coledas, Federico López, Emanuel Toledo y Mariela Yacci, estudiantes del ISPC como evidencia integradora de los módulos de programación y bases de datos.

Fecha de entrega: 08-06-2025
