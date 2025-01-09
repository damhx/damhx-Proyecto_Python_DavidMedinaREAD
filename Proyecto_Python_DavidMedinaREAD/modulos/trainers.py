import json
import os
import modulos.menus as menus
import modulos.campers as campers
import modulos.trainers as trainers

def guardarArchivo(Diccionario,archivo):
    with open (f"./datos/{archivo}.json","w") as salida:
        json.dump(Diccionario, salida)
    return True 

def abrirArchivo(archivo):
    archivoPath = f"./datos/{archivo}.json"
    
    if not os.path.exists(archivoPath):
        print(f"El archivo {archivoPath} no existe.")
        return None 
    with open(archivoPath, "r") as entrada:
        nuevoDiccionario = json.load(entrada)
    return nuevoDiccionario

trainersInfo = abrirArchivo("trainersDataBase")

"""Con esta función se puede verificar que el trainer esté
registrado & darle la bienvenida a la plataforma"""


def ingresarTriner(trainersInfo: dict):
    idIngresadoT = input("Ingrese su documento:) ")
    if idIngresadoT in trainersInfo:
        trainerLogueado = trainersInfo[idIngresadoT]
        nombreT = trainersInfo[idIngresadoT]["nombre"]
        print(f"Bienvenido {nombreT}")
        return trainerLogueado
    else:
        print("ID no registrado")


def opcionesTrainer(trainerLog: dict):
    while True:
        print(menus.menuTrainer)

        opc2Trainers = int(input(":)"))
        match opc2Trainers:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case _:
                break
        break
    




def crearTrainer(trainersInfo: dict):
    nombres = input('Ingrese sus nombres: ').capitalize()
    apellidos = input('Ingrese sus apellidos: ').capitalize()
    numeroDocumento = int(input('Ingrese su número de identificación: '))
    numDoc = str(numeroDocumento)
    if (numDoc not in trainersInfo):
        ruta = "Aun no se ha asignado una ruta"

        trainersInfo[numeroDocumento] = {
            "nombre": nombres,
            "apellidos": apellidos,
            "numeroDocumento": numeroDocumento,
            "ruta": ruta
        }
        guardarArchivo(trainersInfo, "trainersDataBase")
        print(f"Usuario agregado con éxito, tu ID de ingreso es tu número de documento {numeroDocumento}")
    else:
        print(f"El Trainer con número de documento {numeroDocumento} ya existe")
    
    
