import numpy as np 
lista_ruts = []
lista_nombres = []
lista_apellidos = []
lista_fechas = []

platinum = 120000
gold = 80000
silver = 50000
concierto = np.zeros((10,10),int)
def menu():
    print("""" menu
    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir""")

def validar_opcion():
    while True:
        try:           
                opcion = int(input("ingrese opcion: "))
                if opcion in (1,2,3,4,5):
                 return menu
                else:
                    print("ERROR opcion no valida")            
        except:
            print("ERROR debe ingresar numeros enteros")

def validar_nombre():
     nombre = input("ingrese su nombre")
     if len(nombre)>=3 and nombre.isalpha:
          return validar_nombre
     else:
          print("ERROR nombre no valido")
def validar_rut():
     rut = int(input("ingrese su rut sin puntos ni guion"))
     if rut >=999999999:
         return rut
     else:
         print("error rut no valido")
def validar_apellido():
    apellido = input("ingrese su apellido")
    if apellido == len(apellido)>=3:
        return validar_apellido
    else:
        print("ERROR apellido no valido")
contador_ent = 0
def comprar_entradas():
            while True:
                      print(f""" 1.Platinum, ${platinum}. (Asientos del 1 al 20).
                                2.Gold, ${gold}. (Asientos del 21 al 50).
                                3.Silver, ${silver}. (Asientos del 51 al 100).""")
                      opc_comp = int(input("ingrese su opcion"))
                      if opc_comp in (1,2,3):
                           return opc_comp
                      else:
                           print("ERROR debe ingresar una opcion valida")
                           cant_entradas 
                                                         
                
                      rut = int(input("ingrese su rut sin puntos ni guion"))
                      if rut == validar_rut:
                           return nombre
                      else:
                          print("ERROR debe ingresar un rut valido")
                      nombre = input("ingrese su nombre")
                      if nombre == validar_nombre:
                           return apellido
                      else:
                           ("ERROR nombre no valido")
                      apellido = input("ingrese su apellido")
                      if apellido == validar_apellido:
                          return fecha
                      else:
                          print("ERROR fecha no valida")
                      fecha = int(input("ingrese fecha solo con digitos ej: (11/07/2023)"))
                      lista_ruts.append(rut)
                      lista_nombres.append(nombre)
                      lista_apellidos.append(apellido)
                      lista_fechas.append(fecha)
            
 
                

            
           

def mostrar_ubicaciones_dispo():
    print(f" asientos ")
    for x in range (10):
        print(f"{x+1}",end=" ")
        for y in range (10):
            print(f"{concierto+1}",end=" ")
       

def ver_listado_asistentes():
    print(lista_ruts)
    
def mostrar_ganancias_totales():
    print(cont_entradas)
    



cont_entradas = 0
def cant_entradas():
    while True:
        try:
            cant_entradas = int(input("ingrese cantidad de entradas (de 1-3 entradas)"))
            if platinum== 1:
                print(platinum)
            elif platinum ==2:
                print(platinum*2) 
            elif cant_entradas == 3:
               print(platinum*3)
            elif gold== 1:
                print(gold)
            elif gold ==2:
                print(gold*2) 
            elif cant_entradas == 3:
               print(gold*3)
            elif silver== 1:
                print(silver)
            elif silver ==2:
                print(silver*2) 
            elif cant_entradas == 3:
               print(silver*3)
               return
            else:
               print("ERROR opcion incorrecta")

        except:
            print("ERROR debe ingresar numeros enteros")

            