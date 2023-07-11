
import funciones as fn
import numpy

print("""" menu
    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir""")
opcion = fn.validar_opcion

if opcion == 1:
    fn.comprar_entradas
elif opcion == 2:
    fn.mostrar_ubicaciones_dispo
elif opcion == 3:
    fn.ver_listado_asistentes
elif opcion == 4:
    fn.mostrar_ganancias_totales
else:
    pass