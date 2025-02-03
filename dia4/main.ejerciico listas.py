estudiantes = [
    "Adrián Quintero Pinzón" , "Alejandra Pinzón Alvarez", "Ámbar Isabella Plata López",
    "Andrés David Reyes Espinel", "Aura Camila Pico Araque", "Camilo Andrés Suárez Fuentes",
    "Daniel Esteban Guerrero Quintero", "David Santiago Vera Mendez", "Edgar Leonardo Acevedo Arteaga",
    "Gerson Steven Chaparro Martínez", "Harley Yefrey Cabrales Vargas", "John Stiven Negron Regalado",
    "Juan David Saavedra Jaimez", "Juan David Santoyo Jaimes", "Juan David Vargas Soto",
    "Juan Eduardo Pinilla Guzmán", "Juan Fernando Umaña Barragan", "Juan Jose Abril Roman",
    "Maria Juliana Saavedra Mejia", "Mateo Roman Camargo", "Naya Zarela Lizcano Jaimes",
    "Nicolas Chedraui Mantilla", "Omar Fernando Granados Parra", "Santiago Aguilar Vesga",
    "Santiago Andrés Quiñonez Sosa", "Santiago Jaimes Perez", "Sara Sofía Díaz Rodríguez",
    "Sayara Yurley Aparicio Arciniegas", "Sergio Andrés Rueda Hernández", "Simón Dante Salamanca Galvis",
    "Thomas Sebastián Bastos Garcia", "Vladimir Diaz Contreras"
]

booleanito = True
while booleanito:
    print("\nBienvenido al programa de lista de estudiantes")
    print("¿Qué te gustaría hacer?")
    print("1. Agregar estudiante")
    print("2. Ver estudiantes")
    print("3. Editar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir del programa")
    
    opcionUsuario = int(input(": "))
    
    if opcionUsuario == 2:
        # Mostrar la lista de estudiantes
        print("Lista de estudiantes:")
        for i in range(len(estudiantes)):
            print(f"Estudiante #{i + 1}: {estudiantes[i]}")

    elif opcionUsuario == 5:
        # Salir del programa
        print("Saliendo del programa...")
        booleanito = False

    elif opcionUsuario == 1:
        # Agregar nuevo estudiante
        nombreEstudiante = input("¿Qué nombre y apellidos te gustaría agregar al estudiante? (Nombre Apellido): ")
        estudiantes.append(nombreEstudiante)
        print("Lista nueva de estudiantes:")
        for i in range(len(estudiantes)):
            print(f"Estudiante #{i + 1}: {estudiantes[i]}")

    elif opcionUsuario == 3:
        # Editar un estudiante
        print("Lista de estudiantes:")
        for i in range(len(estudiantes)):
            print(f"Estudiante #{i + 1}: {estudiantes[i]}")
        numeroEstudiante = int(input("¿Qué estudiante quieres editar? (Selecciona el número): "))
        
        # Selección para editar nombre o apellido
        print("¿Qué deseas editar?")
        print("1. Editar solo el nombre")
        print("2. Editar solo los apellidos")
        print("3. Editar tanto el nombre como los apellidos")
        
        opcionEdicion = int(input(": "))
        
        if opcionEdicion == 1:
            # Editar solo el nombre
            nombreEstudianteNuevo = input("¿Cuál será el nuevo nombre del estudiante? (Solo el nombre): ")
            partes = estudiantes[numeroEstudiante - 1].split()  # Separar en partes (nombre y apellidos)
            partes[0] = nombreEstudianteNuevo  # Cambiar solo el nombre
            estudiantes[numeroEstudiante - 1] = " ".join(partes)
            print(f"Estudiante #{numeroEstudiante} actualizado: {estudiantes[numeroEstudiante - 1]}")
        
        elif opcionEdicion == 2:
            # Editar solo los apellidos
            apellidosNuevo = input("¿Cuál serán los nuevos apellidos del estudiante? (Solo los apellidos): ")
            partes = estudiantes[numeroEstudiante - 1].split()  # Separar en partes (nombre y apellidos)
            partes[-1] = apellidosNuevo  # Cambiar solo los apellidos
            estudiantes[numeroEstudiante - 1] = " ".join(partes)
            print(f"Estudiante #{numeroEstudiante} actualizado: {estudiantes[numeroEstudiante - 1]}")
        
        elif opcionEdicion == 3:
            # Editar tanto nombre como apellidos
            nombreEstudianteNuevo = input("¿Cuál será el nuevo nombre del estudiante? (Solo el nombre): ")
            apellidosNuevo = input("¿Cuál serán los nuevos apellidos del estudiante? (Solo los apellidos): ")
            estudiantes[numeroEstudiante - 1] = nombreEstudianteNuevo + " " + apellidosNuevo
            print(f"Estudiante #{numeroEstudiante} actualizado: {estudiantes[numeroEstudiante - 1]}")
        
        else:
            print("Opción no válida para edición.")
            
    elif opcionUsuario == 4:
        # Eliminar un estudiante
        print("Lista de estudiantes:")
        for i in range(len(estudiantes)):
            print(f"Estudiante #{i + 1}: {estudiantes[i]}")
        numeroEstudiante = int(input("¿Qué estudiante quieres eliminar? (Selecciona el número): "))
        estudiantes.pop(numeroEstudiante - 1)
        print("Estudiante eliminado.")
        print("Lista de estudiantes actualizada:")
        for i in range(len(estudiantes)):
            print(f"Estudiante #{i + 1}: {estudiantes[i]}")

##Desarollado por Andres Reyes T.i 1097100508