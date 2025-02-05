"""
    Simulacion Academia
    Boceto de ayuda para Reto No1
    
    Herramientas vistas:
    1. Como hacer un Menú interactivo con while
    2. Cada opcion en el Menú, tenga una funcionalidad especifica
    3. Validamos fechas en formato (DD/MM/AAAA) con la funcion -> validar_fecha (En fechas.py se explica todo)
    4. Opcion de 'Agregar' un nuevo estudiante, y agregarlo a un listado General
    5. Opcion de 'Leer' los estudiantes existentes en el listado General
    
"""

listado_Estudiantes = [] #Listado Global

# FUNCIONES --------------------------------------
def agregar_Estudiante(documento, nombre_Estudiante, matricula, notas: list):
    
    estudiante = {} #Creamos un diccionario vacio
    
    """ 
    .update -> Agregar los datos de un estudiante en formato Diccionario {}
    La 'key' sera la cedula del estudiante
    El 'value' sera una lista[] con los datos del estudiante
    """
    estudiante.update({ documento : [nombre_Estudiante, matricula, notas]})
    listado_Estudiantes.append(estudiante)
    return estudiante

def eliminar_Estudiante(listado_Estudiantes: list, llave):
    """
    Funcion que recorre el listado de estudiantes y 
    elimina el estudiante con la llave(documento) ingresado
    """
    
    mensaje_eliminar = f"Estudiante con documento {llave} eliminado"
    mensaje_no_encontrado = f"No hay estudiantes con este documento: {llave}"
    
    for estudiante in listado_Estudiantes:
        if llave in estudiante:
            listado_Estudiantes.remove(estudiante)
            return print(mensaje_eliminar)
    
    return print(mensaje_no_encontrado)

def validar_fecha(fecha):
    """
    Funcion que valida la fecha ingresada en formato (DD/MM/AAAA)
    1. Longitud de 10 caracteres
    2. Los valores de la fecha deben ser numéricos
    3. Los valores de la fecha deben estar entre 1 y 31, 1 y 12 y 1900 y 2025
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
    elif opcion == "1":
        
        documento = int(input("Ingrese el documento del estudiante: "))
        nombre_Estudiante = input("Ingrese el nombre del estudiante: ")
        matricula_Fecha = input("Ingrese la fecha de la matricula (DD/MM/AAAA): ")
        if validar_fecha(matricula_Fecha) != "Fecha válida":
            print("Fecha invalida")
            break
        
        """nota1 = float(input("Ingrese la nota 1: "))
        nota2 = float(input("Ingrese la nota 2: "))
        nota3 = float(input("Ingrese la nota 3: "))
        lista_Notas = [nota1, nota2, nota3]"""
        
        notas = list(map(float, [input("Ingrese la nota 1: "), input("Ingrese la nota 2: "), input("Ingrese la nota 3: ")]))
        
        Dict_Estudiante = agregar_Estudiante(documento, nombre_Estudiante, matricula_Fecha, notas)  
        print("\nAgregado correctamente")
    
    # OPCION 2. Leer
    elif opcion == "2":
        for estudiante in listado_Estudiantes:
            print("\nEstudiante:", estudiante)
            
    # OPCION 3. Eliminar
    elif opcion == "3":
        llave = int(input("Ingrese el documento del estudiante a eliminar: "))
        eliminar_Estudiante(listado_Estudiantes, llave)
             
    elif opcion == "4":
        pass
    
    elif opcion == "5":
        pass
    
    else:
        print("Opcion incorrecta")