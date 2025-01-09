import modulos.menus as menus
import modulos.campers as campers
import modulos.trainers as trainers
import modulos.rutas as rutas
import modulos.grupos as grupos

if __name__ == '__main__':
    while(True):
        print(menus.menuPrincipal)
        print(menus.menuInicio)
        sesion = True
        opMenuInicio = int(input(":)"))
        match opMenuInicio:
            case 1:
                while True:
                    if (sesion==True):
                        print(menus.menuIngreso)
                        opMenuIngreso = int(input(":)"))
                    
                        match opMenuIngreso:
                            case 1:
                                campers.aggCampers(campers.campersInfo)
                                x = input("Presiones cualquier tecla...")
                                break
                            case 2:
                                campLog = campers.ingresarCamper(campers.campersInfo)
                                if (campLog):
                                    
                                    while (sesion == True):
                                        if (campLog["estado"]=='Inscrito' or campLog["estado"]=='Aprobado'):
                                            print(menus.menuCamperInscrito)
                                            opt = int(input(":) "))
                                            match opt:
                                                case 1:
                                                    if (campLog["examen"]==False):
                                                        campers.examenCamper(campLog,campers.campersInfo)
                                                    else:
                                                        input('Usted ya presento la prueba... \nPresione una tecla para volver...')
                                                case 2:
                                                    if(campLog["estado"]=='Inscrito'):
                                                        print(f"Su estado de inscripcion actualmente es {campLog['estado']}\nPresente la prueba para continuar con la inscripción...")
                                                        input('')
                                                    else:
                                                        print(f"Su estado de inscripcion actualmente es {campLog['estado']}\nEspere a que se le asigne una ruta...")
                                                        input('')
                                                case 3:
                                                    sesion = False
                                        elif (campLog["estado"]=='Cursando'):
                                            print(menus.menuCamperCursando)
                                            opt = int(input(":) "))
                                            match opt:
                                                case 1:
                                                    print("Tu horario de clase es ...")
                                                    input("Ingrese una tecla para continuar...")
                                                case 2:
                                                    campers.consultarNotasCamper(grupos.gruposInfo, campLog)
                                                case 3:
                                                    break   
                                           
                            case 3:    
                                break
                            case _:
                                campers.getNume(campers.mensaje)
                    else:
                        break

            #Este case es para los Trainers
            case 2:
                while True:
                    print(menus.menuIngresoTrainer)
                    opMenuIngreso2 = int(input(":)"))
                    match opMenuIngreso2:
                        #Caso para crear un trainer
                        case 1:
                            trainerLog = trainers.ingresarTriner(trainers.trainersInfo)
                            trainers.opcionesTrainer(trainerLog)
                        case 2: 
                            break

            #Este case es para los Coordinadores
            case 3:
                while True:
                    print(menus.menuIngreso)
                    opMenuIngreso3 = int(input(":)"))
                    match opMenuIngreso3:
                        case 1:
                            pass
                        case 2:
                            while True:
                                print(menus.menuCoordinador)
                                opcion = int(input(":)"))
                                match opcion:
                                    case 1:
                                        rutas.crearRuta(rutas.rutaInfo, trainers.trainersInfo)
                                    case 2:
                                        grupos.crearGrupo(grupos.gruposInfo, campers.campersInfo, rutas.rutaInfo)
                                    case 3:
                                        trainers.crearTrainer(trainers.trainersInfo)
                                    case 4:
                                        campers.listarYEvaluarCampers(campers.campersInfo)
                                    case 5:
                                        break
                                    case _:
                                        pass

                        case 3:
                            break