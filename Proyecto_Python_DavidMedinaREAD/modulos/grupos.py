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


gruposInfo = abrirArchivo("gruposDataBase")
camperInfo = abrirArchivo("campersDataBase")
rutaInfo = abrirArchivo("rutasDataBase")

def crearGrupo(gruposInfo: dict, camperInfo: dict, rutaInfo: dict):
    if "grupos" not in gruposInfo:
        gruposInfo["grupos"] = {} 
    
    print("Seleccione una ruta:")
    rutas = rutaInfo["rutas"]
    ruta_list = [
        {"Id": int(doc_id), "ruta_completa": ruta} for doc_id, ruta in rutas.items()
    ]
    
    print("Lista de rutas disponibles:")
    for index, ruta in enumerate(ruta_list):
        print(f"{index+1}. Nombre de la Ruta: {ruta['ruta_completa']['titulo']} - Profesor: {ruta['ruta_completa']['profesor']['nombre']}")
        
    while True:
        seleccion = int(input("Seleccione el índice de la ruta: "))
        if 0 <= (seleccion-1) < len(ruta_list):
            ruta = ruta_list[seleccion-1]["ruta_completa"]
            print(f"Ruta seleccionada: {ruta['titulo']}")
            break
        else:
            print("Índice fuera de rango. Intente nuevamente.")
        print("Por favor ingrese un número válido.")

    profesor_info = ruta["profesor"]
    ruta_sin_profesor = {key: value for key, value in ruta.items() if key != "profesor"}

    # Selección de campers
    print("Seleccione un camper:")
    campers = camperInfo["campers"]
    campers_seleccionados = {}

    while True:
        camper_list = [
            {"Id": doc_id, "nombre": camper["nombre"], "numeroDocumento": camper["numeroDocumento"]}
            for doc_id, camper in campers.items() 
            if camper["haveGrupo"] == False 
        ]
        
        print("Lista de campers disponibles:")
        for index, camper in enumerate(camper_list):
            print(f"{index+1}. Nombre: {camper['nombre']} - Documento: {camper['numeroDocumento']}")
        
        while True:
            seleccion = int(input("Seleccione el índice del camper: "))
            if 0 <= (seleccion-1) < len(camper_list):
                camper = camper_list[seleccion-1]
                print(f"Camper seleccionado: {camper['nombre']} (Documento: {camper['numeroDocumento']})")
                
                doc_id = camper["Id"]
                campers[doc_id]["haveGrupo"] = True  

                campers_seleccionados[doc_id] = {
                    "nombre": camper["nombre"],
                    "numeroDocumento": camper["numeroDocumento"],
                    "ruta": ruta_sin_profesor 
                }
                break  
                
            else:
                print("Índice fuera de rango. Intente nuevamente.")
            print("Por favor ingrese un número válido.")
    
        continuar = input("¿Desea agregar otro camper? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print("\nCampers seleccionados:")
    for camper_id, camper_info in campers_seleccionados.items():
        print(f"- {camper_info['nombre']} (Documento: {camper_info['numeroDocumento']})")

    grupo_id = max(map(int, gruposInfo["grupos"].keys()), default=0) + 1

    gruposInfo["grupos"][grupo_id] = {
        "profesor": profesor_info, 
        "campers": campers_seleccionados 
    }


    guardarArchivo(gruposInfo, "gruposDataBase")
    print(f"El grupo {gruposInfo['grupos'][grupo_id]} ha sido creado con exito")
