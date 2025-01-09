import json
import os
import modulos.menus as menus

def guardarArchivo(Diccionario,archivo):
    with open (f"./datos/{archivo}.json","w") as salida:
        json.dump(Diccionario, salida)
    return True 

def abrirArchivo(archivo):
    arcPath = f"./datos/{archivo}.json"
    
    if not os.path.exists(arcPath):
        print(f"El archivo {arcPath} no existe.")
        return None
    
    with open(arcPath, "r") as entrada:
        nuevoDiccionario = json.load(entrada)
    return nuevoDiccionario

rutaInfo = abrirArchivo("rutasDataBase")
coordinadorInfo = abrirArchivo("coordinadoresDataInfo")
camperInfo = abrirArchivo("campersDataBase")
trainerInfo = abrirArchivo("trainersDataBase")

def crearRuta(rutaInfo: dict, trainerInfo: dict):
    ruta_id = max(map(int, rutaInfo["rutas"].keys()), default=0) + 1
    
    # Selección de Fundamentos de Programación
    while True:
        funProgramacion = int(input('Para Fundamentos de Programacion, ¿Que modulo elije?\n1. Introduccion a la Algoritmia\n2. Python\n3. PSeInt\n'))
        match funProgramacion:
            case 1:
                funProgramacion = {
                    "titulo": "Introduccion a la algoritmia",
                    "notas": [0, 0, 0]
                }
                break
            case 2:
                funProgramacion = {
                    "titulo": "Python",
                    "notas": [0, 0, 0]
                }
                break
            case 3:
                funProgramacion = {
                    "titulo": "PSeInt",
                    "notas": [0, 0, 0]
                }
                break
            case _:
                input("Ingrese una opcion valida...")
                continue

    # Programación Web
    proWeb = "Programación Web (HTML, CSS y Bootstrap)"

    # Selección de Programación Formal
    while True:
        proFormal = int(input('Para Programacion formal, ¿Que modulo elije?\n1. Java\n2. JavaScript\n3. C#\n'))
        match proFormal:
            case 1:
                proFormal = {
                    "titulo": "Java",
                    "notas": [0, 0, 0]
                }
                break
            case 2:
                proFormal = {
                    "titulo": "JavaScript",
                    "notas": [0, 0, 0]
                }
                break
            case 3:
                proFormal = {
                    "titulo": "C#",
                    "notas": [0, 0, 0]
                }
                break
            case _:
                input("Ingrese una opcion valida...")
                continue

    # Selección de Bases de Datos
    while True:
        baseDatos = int(input('Para Bases de Datos, ¿Que modulo elije?\n1. Mysql\n2. MongoDb\n3. Postgresql\n'))
        match baseDatos:
            case 1:
                baseDatos = {
                    "titulo": "Mysql",
                    "notas": [0, 0, 0]
                }
                break
            case 2:
                baseDatos = {
                    "titulo": "MongoDb",
                    "notas": [0, 0, 0]
                }
                break
            case 3:
                baseDatos = {
                    "titulo": "Postgresql",
                    "notas": [0, 0, 0]
                }
                break
            case _:
                input("Ingrese una opcion valida...")
                continue

    # Selección de BackEnd
    while True:
        back = int(input('Para BackEnd, ¿Que modulo elije?\n1. NetCore\n2. Spring Boot\n3. NodeJS y Express\n'))
        match back:
            case 1:
                back = {
                    "titulo": "NetCore",
                    "notas": [0, 0, 0]
                }
                break
            case 2:
                back = {
                    "titulo": "Spring Boot",
                    "notas": [0, 0, 0]
                }
                break
            case 3:
                back = {
                    "titulo": "NodeJS y Express",
                    "notas": [0, 0, 0]
                }
                break
            case _:
                input("Ingrese una opcion valida...")
                continue

    print("Seleccione un trainer:")
    trainers_asignados = {ruta["profesor"]["numeroDocumento"] for ruta in rutaInfo["rutas"].values()}
    trainers_list = [
        {"numeroDocumento": int(doc_id), "nombre": trainer["nombre"]}
        for doc_id, trainer in trainerInfo.items() if int(doc_id) not in trainers_asignados
    ]

    if not trainers_list:
        print("No hay trainers disponibles para asignar a esta ruta.")
        return

    print("Lista de trainers:")
    for index, trainer in enumerate(trainers_list):
        print(f"{index+1}. Nombre: {trainer['nombre']}")

    while True:
        seleccion = int(input("Seleccione el índice del trainer: "))
        if 0 <= (seleccion-1) < len(trainers_list):
            profe = trainers_list[seleccion-1]
            print(f"Trainer seleccionado: {profe['nombre']} (Documento: {profe['numeroDocumento']})")
            break
        else:
            print("Índice fuera de rango. Intente nuevamente.")

    # Ingresar nombre de la ruta
    titulo = input("Ingrese nombre de la ruta: ")

    # Guardar la ruta
    rutaInfo["rutas"][ruta_id] = {
        "titulo": titulo,
        "funProgram": funProgramacion,
        "proWeb": proWeb,
        "proFormal": proFormal,
        "baseDatos": baseDatos,
        "back": back,
        "profesor": profe
    }

    guardarArchivo(rutaInfo, "rutasDataBase")
    print(f"La ruta #{ruta_id} ha sido agregada con éxito.")
