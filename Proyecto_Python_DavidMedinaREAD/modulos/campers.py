import json
import os
import modulos.menus as menus

def getNume(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero   
        except Exception:
            print("Opción no válida, por favor ingrese un valor valido: ")

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
 
"""Con esta función se permite que el camper se registre y sus
datos sean guardados en el archivo campersDataBase.json"""
campersInfo = abrirArchivo("campersDataBase")

def aggCampers(campersInfo: dict):
    print("REGISTRATE: ")
    nombres = input("Ingrese sus nombres: ").capitalize()
    apellidos = input("Ingrese sus apellidos: ").capitalize()

    numeroDocumento = int(input("Ingrese su número de identificación: "))
    numDoc = str(numeroDocumento)
    
    if numDoc not in campersInfo["campers"]: 
        direccion = input("Ingrese su dirección: ").capitalize()
        acudiente = input("Ingrese el nombre de su acudiente: ").capitalize()
        telefonoMovil = int(input("Ingrese su número de teléfono móvil: "))
        telefonoFijo = int(input("Ingrese su número de teléfono fijo (Si no aplica, digite 0): "))

        campersInfo["campers"][numDoc] = {
            "nombre": nombres,
            "apellidos": apellidos,
            "numeroDocumento": numeroDocumento,
            "direccion": direccion,
            "acudiente": acudiente,
            "telefonos": {
                "celular": telefonoMovil,
                "fijo": telefonoFijo,
            },
            "estado": "Inscrito", 
            "examen": False,
            "haveGrupo": False,
            "riesgo": "ninguno",   
            "notas": {
                "teorica": 0,
                "practica": 0,
                "quizes": 0
            }
        }

        guardarArchivo(campersInfo, "campersDataBase")  # Guardar los datos actualizados
        print(f"Usuario agregado con éxito, tu ID de ingreso es tu número de documento {numeroDocumento}")
        abrirArchivo("campersDataBase")
    else:
        print(f"El número de documento {numeroDocumento} ya se encuentra registrado.")

        

"""Con esa función se puede verificar que el Camper estéabrirArchivo("campersDataBase")
registrado & darle la bienvenidad a la plataforma"""
def ingresarCamper(campersInfo: dict):
    print("Ingrese su ID para continuar: ")
    idIngresado = input(':)')
    if idIngresado in campersInfo["campers"]:
        camperEncontrado = campersInfo["campers"][idIngresado]
        nombre = (campersInfo["campers"][idIngresado]["nombre"]) + " " + (campersInfo["campers"][idIngresado]["apellidos"])
        print(f"***Bienvenido {nombre}***")     
        return camperEncontrado         
    else:
        print("Usuario no encontrado.")



def aggGrupo(campersInfo: dict):
    grupo = input("Ingrese el Grupo al que desea agregar al estudiante: ")
    estudiante = (input("Ingrese el documento del estudiante a agregar: "))

    """Verificar que el estudiante y el grupo existan"""
    if estudiante in campersInfo and grupo in campersInfo:
        """Obtener el subdiccionario de estudiantes en el grupo"""
        estudiantes = campersInfo[grupo]["estudiantes"]
        
        """Verificar si el grupo tiene menos de 33 estudiantes"""
        if len(estudiantes) < 33:
            """Agregar el estudiante al grupo"""
            estudiantes[estudiante] = campersInfo[estudiante]
            """ELiminar del diccionario de campers y queda en el dicccionario del grupo"""
            del campersInfo[estudiante]
            print(f"Estudiante {estudiante} agregado al grupo {grupo}.")
        else:
            print(f"El grupo {grupo} se encuentra completo.")
    else:
        print("El estudiante o el grupo no existen.")
    guardarArchivo(campersInfo, "campersDataBase")
    return aggGrupo





def aggNotas(campersInfo: dict):
    grupo = input("Ingrese el grupo al que va a agregar notas: ")
    estudiante = input("Ingrese documento del estudiante al que desea agregarle notas: ")

    if grupo in campersInfo and estudiante in campersInfo[grupo]["estudiantes"]:
        
        estudianteInfo = campersInfo[grupo]["estudiantes"][estudiante]
        print("Datos del estudiante:", estudianteInfo)
        notaTeorica = float(input("Ingrese nota teórica: "))
        notaPractica = float(input("Ingrese nota práctica: "))
        notaQuizes = float(input("Ingrese nota de los quizes: "))

        estudianteInfo["notas"]["teorica"] = notaTeorica
        estudianteInfo["notas"]["practica"] = notaPractica
        estudianteInfo["notas"]["quizes"] = notaQuizes

        print("Notas actualizadas correctamente:", estudianteInfo["notas"])
    else:
       
        print("Error: Grupo o estudiante no encontrado.")
    guardarArchivo(campersInfo, "campersDataBase")
    return aggNotas

def subirAdmision(campersInfo: dict):
    estudiante = input("Ingrese el documento del estudiante al que desea subir notas: ")

    if estudiante in campersInfo:

        notaTeoricaF = int(input("Ingrese la nota de la evaluacion teorica: "))
        notaPracticaF = int(input("Ingrese la nota de la evaluacion practica:  "))

        notasTotal = (notaTeoricaF * 0.5) + (notaPracticaF * 0.5)
        if notasTotal > 60:
            campersInfo[estudiante]["estado"]["En proceso"] = False
            campersInfo[estudiante]["estado"]["Inscrito"] = True
            print(f"Notas aprobadas. Total: {notasTotal}")
        else:
            print("La persona no pasó el filtro")
    else:
          print("Estudiante no encontrado")
    guardarArchivo(campersInfo, "campersDataBase")
    return subirAdmision



def listarYEvaluarCampers(campersInfo: dict):
    campers_inscritos = [
        {
            "indice": index + 1,
            "numeroDocumento": camper["numeroDocumento"],
            "nombre": camper["nombre"],
            "apellidos": camper["apellidos"]
        }
        for index, camper in enumerate(campersInfo["campers"].values())
        if camper["estado"] == "Inscrito"
    ]

    if not campers_inscritos:
        print("No hay campers con estado 'Inscrito'.")
        return

    print("Lista de campers inscritos:")
    for camper in campers_inscritos:
        print(f"{camper['indice']}. Documento: {camper['numeroDocumento']} - Nombre: {camper['nombre']} {camper['apellidos']}")

    while True:
        seleccion = int(input("Seleccione el índice del camper: "))
        if 1 <= seleccion <= len(campers_inscritos):
            camper_seleccionado = campers_inscritos[seleccion - 1]
            print(f"Has seleccionado al camper: {camper_seleccionado['nombre']} {camper_seleccionado['apellidos']} (Documento: {camper_seleccionado['numeroDocumento']})")
            break
        else:
            print("Índice fuera de rango. Intente nuevamente.")
        print("Por favor, ingrese un número válido.")

    # Realizar el examen
    print("\nResponda de 0 a 10 las siguientes preguntas\n")
    while True:
        try:
            rta1 = int(input("¿Le gusta el Ping Pong? "))
            if 0 <= rta1 <= 10:
                break
            else:
                print("Ingrese un valor válido (entre 0 y 10).")
        except ValueError:
            print("Ingrese un número válido.")

    while True:
        try:
            rta2 = int(input("¿Entró a programación por plata? "))
            if 0 <= rta2 <= 10:
                break
            else:
                print("Ingrese un valor válido (entre 0 y 10).")
        except ValueError:
            print("Ingrese un número válido.")

    while True:
        try:
            rta3 = int(input("Pregunta gratis, marque 10 "))
            if 0 <= rta3 <= 10:
                break
            else:
                print("Ingrese un valor válido (entre 0 y 10).")
        except ValueError:
            print("Ingrese un número válido.")

    # Calcular la nota final
    notaFinal = (rta1 + rta2 + rta3) / 3
    camperDocumento = str(camper_seleccionado["numeroDocumento"])

    # Actualizar la información del camper
    campersInfo["campers"][camperDocumento]["examen"] = notaFinal
    if notaFinal >= 7:
        campersInfo["campers"][camperDocumento]["estado"] = "Aprobado"
        print(f"\n¡Felicidades! {camper_seleccionado['nombre']} {camper_seleccionado['apellidos']} ha aprobado el examen con una nota de {notaFinal:.2f}.")
    else:
        print(f"\nLo sentimos. {camper_seleccionado['nombre']} {camper_seleccionado['apellidos']} no aprobó el examen. Su nota es {notaFinal:.2f}.")

    # Guardar los cambios
    guardarArchivo(campersInfo, "campersDataBase")
    abrirArchivo("campersDataBase")


def consultarNotasCamper(gruposInfo: dict, campLog: dict):
    # Pedir el ID del camper
    camper_id = campLog['numeroDocumento']
    
    # Buscar el grupo en el que está el camper
    grupo_encontrado = None
    for grupo_id, grupo in gruposInfo["grupos"].items():
        if camper_id in grupo["campers"]:
            grupo_encontrado = {
                "grupo_id": grupo_id,
                "camper": grupo["campers"][camper_id]
            }
            break

    if not grupo_encontrado:
        print(f"El camper con ID {camper_id} no está registrado en ningún grupo.")
        return

    # Mostrar información del grupo y el camper
    camper_info = grupo_encontrado["camper"]
    print(f"\nEl camper con ID {camper_id} está en el grupo {grupo_encontrado['grupo_id']}.")
    print(f"Nombre: {camper_info['nombre']}")
    print(f"Ruta: {camper_info['ruta']['titulo']}")

    # Listar las materias disponibles
    materias = camper_info["ruta"]
    materias_claves = ["funProgram", "proWeb", "proFormal", "baseDatos", "back"]

    print("\nMaterias disponibles para consultar notas:")
    for idx, clave in enumerate(materias_claves, start=1):
        if clave in materias:
            print(f"{idx}. {materias[clave]['titulo'] if isinstance(materias[clave], dict) else materias[clave]}")

    # Seleccionar la materia
    while True:
        try:
            seleccion = int(input("\nSeleccione el índice de la materia: "))
            if 1 <= seleccion <= len(materias_claves):
                materia_clave = materias_claves[seleccion - 1]
                if isinstance(materias[materia_clave], dict):  # Si la materia tiene notas
                    materia = materias[materia_clave]
                    print(f"\nNotas para {materia['titulo']}: {materia['notas']}")
                else:  # Materias sin notas
                    print(f"\nLa materia seleccionada no tiene notas asociadas: {materias[materia_clave]}")
                break
            else:
                print("Índice fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Por favor ingrese un número válido.")


