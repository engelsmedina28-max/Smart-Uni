nombre = ""
correo = ""
contraseña = ""
edad = ""
carrera = ""
año_de_estudio = ""
cuenta_creada = False

datos_usuario = []
horario = [
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""]
]
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
horas = ["07:00", "09:00", "11:00", "13:00", "15:00"]


examenes = [["Matemáticas", "17 feb"], ["Programación", "20 feb"]]
recordatorios = [["Entregar tarea de Cálculo", "Mañana"], ["Inscripción abierta", "Hasta el primero de marzo"]]
ultimos_apuntes = [["Álgebra - PDF", "Ana M."], ["Redes - Resumen", "Carlos R."]]
tip_del_dia = "Organiza tus apuntes en la biblioteca de Smart Uni para llevar un mejor control y acceso rapido."

listas_tareas = [
    "DISEÑO Y MAQUETACION",
    "PROYECTO INTEGRADOR",
    "PROGRAM. ESTRUCTURADA",
    "HABILIDADES DE COMUNICACION",
    "ACTIVIDAD ESTUDIANTIL I",
    "CÁLCULO",
    "HISTORIA",
    "FUNDAMENTOS DE INFORMATICA"
]

apuntes = [
    ["Habilidades de Comunicación", "Expresión y Liderazgo", "2do Semestre"],
    ["Actividad estudiantil", "Actividad estudiantil", "2do Semestre"],
    ["Diseño y maquetación", "Fundamentos", "2do Semestre"],
    ["Fundamentos de la Informática", "Informática", "2do Semestre"]
]

categorias_material = ["Apuntes", "PDF", "Videos", "Enlaces", "Prácticas", "Presentaciones", "Estudio", "Información"]


def registrar_usuario():
    global nombre, correo, contraseña, edad, carrera, año_de_estudio, cuenta_creada
    print("______________Crear Cuenta_______________")
    print("Registro de Estudiante - UNAN-León")
    while True:
        try:
            nombre = input("Ingrese su Nombre Completo: ")
            if not nombre.replace(" ", "").isalpha():
                raise ValueError("El nombre debe contener solo letras.")
            break
        except ValueError as error:
            print("Error:", error)

    while True:
        try:
            correo = input("Ingrese su Correo Institucional: ")
            if "@" not in correo:
                raise ValueError("El correo debe contener el símbolo @.")
            if correo.count("@") > 1:
                raise ValueError("El correo debe tener un solo símbolo @.")
            if correo.split("@")[0].strip() == "":
                raise ValueError("El correo debe llevar texto antes del @.")
            partes = correo.split("@")[1].split(".")
            if len(partes) > 3 or "" in partes:
                raise ValueError("Después del @ debe haber de 1 a 3 palabras separadas por puntos.")
            if correo.endswith("@gmail.com") or correo.endswith("@outlook.com") or correo.endswith("@hotmail.com"):
                raise ValueError("El correo debe ser institucional.")
            break
        except ValueError as error:
            print("Error:", error)

    while True:
        try:

            print("Seleccione su Carrera:")

            print("1. Ingeniería de Sistemas")
            print("2. Ingeniería en Telemática")
            print("3. Ingeniería Estadística")
            print("4. Licenciatura en Matemática")

            opcion_carrera = int(input("Ingrese el número de su carrera: "))

            if opcion_carrera < 1 or opcion_carrera > 4:
                raise ValueError("Seleccione un número entre 1 y 4.")

            if opcion_carrera == 1:
                carrera = "Ingeniería de Sistemas"
                max_años = 5
            elif opcion_carrera == 2:
                carrera = "Ingeniería en Telemática"
                max_años = 5
            elif opcion_carrera == 3:
                carrera = "Ingeniería Estadística"
                max_años = 5
            elif opcion_carrera == 4:
                carrera = "Licenciatura en Matemática"
                max_años = 5

            break

        except ValueError as error:
            print("Error:", error)

    while True:
        try:
            contraseña = input("Ingrese su Contraseña (mínimo 8 caracteres): ")
            if len(contraseña) < 8:
                raise ValueError("La contraseña debe tener mínimo 8 caracteres.")
            break
        except ValueError as error:
            print("Error:", error)

    while True:
        try:
            confirmar_contraseña = input("Confirme su Contraseña: ")
            if confirmar_contraseña != contraseña:
                raise ValueError("La contraseña no coincide con la anterior. Hagalo de nuevo: ")
            break
        except ValueError as error:
            print("Error:", error)

    while True:
        try:
            edad = int(input("Ingrese su Edad: "))
            if edad < 16 or edad > 100:
                raise ValueError("Ingrese una edad válida.")
            break
        except ValueError as error:
            print("Error:", error)

    while True:
        try:
            año_de_estudio = int(input("¿Qué año de su carrera está cursando actualmente? (escriba un número del 1 al " + str(max_años) + "): "))
            if año_de_estudio <= 0 or año_de_estudio > max_años:
                raise ValueError("Ese año no existe en su carrera. Escriba un número del 1 al " + str(max_años) + ".")
            break
        except ValueError as error:
            print("Error:", error)

    datos_usuario.extend([nombre, correo, contraseña, edad, carrera, año_de_estudio])
    cuenta_creada = True


def iniciar_sesion():
    while True:
        try:
            print("________________________Iniciar Sesion________________________")
            print("(Escriba 0 en el correo para volver al menu)")
            correo_ingresado = input("Ingrese su Correo Institucional: ")
            if correo_ingresado == "0":
                return False
            contraseña_ingresada = input("Ingrese su Contraseña: ")

            if correo_ingresado == correo and contraseña_ingresada == contraseña:
                print("Inicio de Sesion Exitosa")
                break
            else:
                raise ValueError("Correo o Contraseña Incorrectos. Intente de nuevo.")

        except ValueError as error:
            print("Error:", error)
    return True


def perfil():

    print("________________Bienvenido ya estas dentro de Smart Uni tu asistente universitario_______________")
    print("____________________________________________________________________________________________________________")
    print("Tu asistente personal Universitario")
    print("============TU PERFIL==========")
    print("Nombre: ", nombre)
    print("Correo: ", correo)
    print("Edad: ", edad)
    print("Carrera: ", carrera)
    print("Año de Estudio: ", año_de_estudio)
    print("____________________________________________________________________________________________________________")
    print("                                                                                                  ")
    print("ESTE ES NUESTRO PROYECTO INTEGRADOR SMARTUNI ASISTENTE PERSONAL UNIVERSITARIO ESPERAMOS SEA DE SU AGRADO")
    while True:
        print()
        print(nombre, "-", "Año", año_de_estudio, "-", carrera)
        print("1. Materias (agregar una clase)")
        print("2. Calendario (ver clases)")
        print("3. Amigos")
        print("4. Tareas")
        print("5. Apuntes")
        print("6. Material")
        print("7. Inicio")
        print("8. Asistente")
        print("9. Cerrar Sesion")

        try:
            opcion_perfil = input("Ingrese el numero de la opcion que desea realizar: ")
            if opcion_perfil not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                raise ValueError("Escriba solo un numero del 1 al 9. No se permiten letras ni otros simbolos.")
        except ValueError as error:
            print("Error:", error)
            continue

        if opcion_perfil == "1":
            agregar_clase()
        elif opcion_perfil == "2":
            ver_clases()
        elif opcion_perfil == "3":
            ver_amigos()
        elif opcion_perfil == "4":
            ver_tareas()
        elif opcion_perfil == "5":
            ver_apuntes()
        elif opcion_perfil == "6":
            ver_material()
        elif opcion_perfil == "7":
            ver_inicio()
        elif opcion_perfil == "8":
            ver_asistente()
        elif opcion_perfil == "9":
            break
        else:
            print("Opcion no valida.")


def agregar_clase():
    while True:
        try:
            print("Dias: 1.Lunes 2.Martes 3.Miercoles 4.Jueves 5.Viernes (0 para cancelar)")
            d = int(input("Ingrese el numero del dia: "))
            if d == 0:
                break
            print("Horas: 1.07:00 2.09:00 3.11:00 4.13:00 5.15:00")
            h = int(input("Ingrese el numero de la hora: "))
            if d < 1 or d > 5 or h < 1 or h > 5:
                raise ValueError("Numero fuera de rango.")
            if horario[h - 1][d - 1] != "":
                raise ValueError("Ya hay una clase en ese horario.")
            materia = input("Ingrese la materia: ")
            if materia.strip() == "":
                raise ValueError("La materia no puede estar vacia.")
            horario[h - 1][d - 1] = materia
            print("Clase agregada.")
            break
        except ValueError as error:
            print("Error:", error)


def ver_clases():
    print()
    print("============TUS CLASES==========")
    hay_clases = False
    for i in range(5):
        for j in range(5):
            if horario[i][j] != "":
                print(dias[j], horas[i], "-", horario[i][j])
                hay_clases = True
    if hay_clases == False:
        print("No tienes clases agregadas.")
    print("================================")


def ver_inicio():
    print()
    print("============TU ASISTENTE PERSONAL UNIVERSITARIO==========")
    print("--- Proximos examenes ---")
    for examen in examenes:
        print("-", examen[0], "|", examen[1])
    print("--- Recordatorios ---")
    for recordatorio in recordatorios:
        print("-", recordatorio[0], "|", recordatorio[1])
    print("--- Ultimos Apuntes (3 feb) ---")
    for apunte in ultimos_apuntes:
        print("-", apunte[0], "|", apunte[1])
    print("--- Tips del Dia ---")
    print(tip_del_dia)
    print("=======================================================")


def ver_amigos():
    print()
    print("============AMIGOS==========")
    print("Aun no tienes amigos agregados.")
    print("============================")


def ver_tareas():
    print()
    print("============TAREAS==========")
    print("TODAS MIS TAREAS")
    for i in range(len(listas_tareas)):
        print(str(i + 1) + ". " + listas_tareas[i])
    print("============================")


def ver_apuntes():
    print()
    print("============APUNTES==========")
    print("Encuentra y comparte apuntes de tus materias")
    for apunte in apuntes:
        print("-", apunte[0])
        print("     Tema:", apunte[1])
        print("     Semestre:", apunte[2])
    print("=============================")


def ver_material():
    print()
    print("============MATERIAL==========")
    for i in range(len(categorias_material)):
        print(str(i + 1) + ". " + categorias_material[i])
    print("==============================")


def ver_asistente():
    print()
    print("============ASISTENTE SMART UNI==========")
    print("¿Como puedo ayudarte hoy?")
    print("=========================================")


print("_______________________Smart Uni_______________________")
print("---Bienvenido a tu Asistente Personal Universitario---")

while True:

    print()
    print("Elije una de las siguientes opciones:")
    print("1. Crear una cuenta nueva")
    print("2. Iniciar Sesion")
    print("3. Salir del Programa")

    try:
        opcion = input("Ingrese el numero de la opcion que desea realizar: ")
        if opcion not in ["1", "2", "3"]:
            raise ValueError("Escriba solo el numero 1, 2 o 3. No se permiten letras ni otros simbolos.")
    except ValueError as error:
        print("Error:", error)
        continue

    if opcion == "1":

        if cuenta_creada == True:
            print("Ya tienes una cuenta creada.")
        else:
            registrar_usuario()
            print("Cuenta creada exitosamente.")

    elif opcion == "2":

        if cuenta_creada == False:
            print("Primero debes registrarte.")
        else:
            if iniciar_sesion() == True:
                perfil()

    elif opcion == "3":

        print("Gracias por usar SmartUni, hasta luego.")
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida.")