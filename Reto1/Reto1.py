"""
    Simulacion Academia
    Boceto de ayuda para Reto No1
    
    Herramientas vistas:
    1. Como hacer un Menú interactivo con while
    2. Cada opcion en el Menú, tenga una funcionalidad especifica
    3. Validamos fechas en formato (DD/MM/AAAA) con la funcion -> validar_fecha (En fechas.py se explica todo)
    4. Opcion de 'Agregar' un nuevo estudiante, y agregarlo a un listado General
    5. Opcion de 'Leer' los estudiantes existentes en el listado General
    
    Tarea: 
    Agregar una funcion para sacar 'promedio' con las notas que tenga el estudiante
"""

listado_Estudiantes = []

# FUNCIONES --------------------------------------
def agregar_Estudiante(documento, nombre_Estudiante, matricula, notas: list):
    
    estudiante = {} #Creamos un diccionario vacio
    
    """ 
    .update -> Agregar los datos de un estudiante en formato Diccionario {}
    La 'key' sera la cedula del estudiante
    El 'value' sera una lista[] con los datos del estudiante
    """
    estudiante.update({ documento : [nombre_Estudiante, matricula, notas]})
    return estudiante

def agregar_A_Listado(datos_Estudiante: dict):
    
    """
    Agrega el diccionario datos_Estudiante -> al listado general -> listado_Estudiantes
    con la opcion 2. del menu podremos ver todos los estudiantes por consola
    """
    
    listado_Estudiantes.append(datos_Estudiante)
    return listado_Estudiantes

def validar_fecha(fecha):
    """
    Recuerda que esta función se explica en detalle en fechas.py. Ahí esta documentado ;)
    """
    
    dia, mes, anio = fecha.split("/")

    if len(fecha) != 10:
        return "Fecha invalida. Formato incorrecto"

    if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
        return "Fecha invalida. Los valores de la fecha no son numéricos"

    dia, mes, anio = int(dia), int(mes), int(anio)

    if not (1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= anio <= 2025):
        return "Fecha invalida. El día, mes o año es incorrecto"

    return "Fecha válida"

# MENU ---------------------------------------------

while True:
    print("\nMenu Academia")
    print("1. Agregar")
    print("2. Leer")
    print("3. Eliminar")
    print("4. Operaciones")
    print("5. Comparacion")
    print("6. Salir")
    
    opcion = input("Elige una opcion (1-6): ")
    
    if opcion == "6":
        print("Adios !")
        break
    
    # OPCION 1. Agregar
    if opcion == "1":
        
        documento = int(input("Ingrese el documento del estudiante: "))
        nombre_Estudiante = input("Ingrese el nombre del estudiante: ")
        matricula_Fecha = input("Ingrese la fecha de la matricula (DD/MM/AAAA): ")
        
        nota1 = float(input("Ingrese la nota 1: "))
        nota2 = float(input("Ingrese la nota 2: "))
        nota3 = float(input("Ingrese la nota 3: "))
        lista_Notas = [nota1, nota2, nota3]   
        
        Dict_Estudiante = agregar_Estudiante(documento, nombre_Estudiante, matricula_Fecha, lista_Notas)  
        agregar_A_Listado(Dict_Estudiante) # Inmediatamente agregamos el estudiante creado al listado general   
        print("\nAgregado correctamente")
    
    # OPCION 2. Leer
    if opcion == "2":
        for estudiante in listado_Estudiantes:
            print("Estudiante: ", estudiante)
             
    else:
        print("ERROR. Ingrese una opcion valida")