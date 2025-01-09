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

coordinadorInfo = abrirArchivo("coordinadoresDataInfo")
camperInfo = abrirArchivo("campersDataBase")
rutasInfo = abrirArchivo("rutasDataBase")

def crearCoordinador(coordinadorInfo: dict):
    nombres = input('Ingrese sus nombres: ').capitalize()
    apellidos = input('Ingrese sus apellidos: ').capitalize()
    numeroDocumento = int(input('Ingrese su número de identificación: '))
    numDoc = str(numeroDocumento)
    if (numDoc not in coordinadorInfo):
        coordinadorInfo[numeroDocumento] = {
            "nombre": nombres,
            "apellidos": apellidos,
            "numeroDocumento": numeroDocumento,
        }
        guardarArchivo(coordinadorInfo, "trainersDataBase")
        print(f"Usuario agregado con éxito, tu ID de ingreso es tu número de documento {numeroDocumento}")
    else:
        print(f"El Trainer con número de documento {numeroDocumento} ya existe")
    

def ingresarCoordinador(coordinadorInfo: dict):
    print("Ingrese su ID para continuar: ")
    idIngresado = input(':)')
    if idIngresado in coordinadorInfo:
        coordinadorEncontrado = coordinadorInfo[idIngresado]
        nombre = coordinadorInfo[idIngresado]["nombre"] + " " + coordinadorInfo[idIngresado]["apellidos"] 
        print(f"***Bienvenido {nombre}***")    
        return coordinadorEncontrado                   
    else:
        print("Usuario no encontrado.")
    

