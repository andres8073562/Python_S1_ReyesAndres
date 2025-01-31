Algoritmo jornadadevacunacion
		
		DEFINIR fiebreAmarillaNinos, fiebreAmarillaAdultos COMO ENTERO 
		DEFINIR varicelaNinos, varicelaAdultos COMO ENTERO 
		DEFINIR rubeolaNinos, rubeolaAdultos COMO ENTERO 
		DEFINIR meningococoNinos, meningococoAdultos COMO ENTERO 
		DEFINIR influenzaNinos, influenzaAdultos COMO ENTERO 
		DEFINIR hepatitisANinos, hepatitisAAdultos COMO ENTERO 
		DEFINIR tetanoNinos, tetanoAdultos COMO ENTERO 
		DEFINIR difteriaNinos, difteriaAdultos COMO ENTERO
		DEFINIR totalVacunas COMO ENTERO 
		DEFINIR opcion, edad COMO ENTERO
		fiebreAmarillaNinos<-0
		fiebreAmarillaAdultos<-0
		varicelaNinos<-0
		varicelaAdultos<-0
		rubeolaNinos<-0
		rubeolaAdultos<-0
		meningococoNinos<-0
		meningococoAdultos<-0
		influenzaNinos<-0
		influenzaAdultos<-0
		hepatitisANinos<-0
		hepatitisAAdultos<-0
		tetanoNinos<-0
		tetanoAdultos<-0
		difteriaNinos<-0
		difteriaAdultos<-0
		totalVacunas<-0
		
		MIENTRAS VERDADERO HACER
			ESCRIBIR "Jornada de vacunación - Centro de Salud de Floridablanca"
			ESCRIBIR "Seleccione el tipo de vacuna aplicada (0 para finalizar):"
			ESCRIBIR "1. Fiebre Amarilla"
			ESCRIBIR "2. Varicela"
			ESCRIBIR "3. Rubeola"
			ESCRIBIR "4. Meningococo (solo para niños < 10 años)"
			ESCRIBIR "5. Influenza"
			ESCRIBIR "6. Sarampión"
			ESCRIBIR "7. Hepatitis A"
			ESCRIBIR "8. Tétano"
			ESCRIBIR "9. Difteria"
			LEER opcion
			
			SI opcion = 0 ENTONCES
				Escribir "SALIR"
			FIN SI
			
			ESCRIBIR "Ingrese la edad de la persona vacunada:"
			LEER edad
			
			
			SI edad < 18 ENTONCES
				ESCRIBIR "La persona es un niño."
				SEGÚN opcion HACER
			CASO 1:
				fiebreAmarillaNinos <- fiebreAmarillaNinos + 1
			CASO 2:
				varicelaNinos <- varicelaNinos + 1
			CASO 3:
				rubeolaNinos <- rubeolaNinos + 1
			CASO 4:
				SI edad < 10 ENTONCES
					meningococoNinos <- meningococoNinos + 1
				SINO
					ESCRIBIR "La vacuna meningococo es solo para niños menores de 10 años."
				FIN SI
			CASO 5:
				influenzaNinos <- influenzaNinos + 1
			CASO 6:
				sarampionNinos <- sarampionNinos + 1
			CASO 7:
				hepatitisANinos <- hepatitisANinos + 1
			CASO 8:
				tetanoNinos <- tetanoNinos + 1
			CASO 9:
				difteriaNinos <- difteriaNinos + 1
			CASO CONTRARIO:
				ESCRIBIR "Opción no válida."
		FIN SEGÚN
	SINO
		ESCRIBIR "La persona es un adulto."
		SEGÚN opcion HACER
	CASO 1:
		fiebreAmarillaAdultos <- fiebreAmarillaAdultos + 1
	CASO 2:
		varicelaAdultos <- varicelaAdultos + 1
	CASO 3:
		rubeolaAdultos <- rubeolaAdultos + 1
	CASO 4:
		ESCRIBIR "La vacuna meningococo es solo para niños menores de 10 años. No se aplicará."
	CASO 5:
		influenzaAdultos <- influenzaAdultos + 1
	CASO 6:
		sarampionAdultos <- sarampionAdultos + 1
	CASO 7:
		hepatitisAAdultos <- hepatitisAAdultos + 1
	CASO 8:
		tetanoAdultos <- tetanoAdultos + 1
	CASO 9:
		difteriaAdultos <- difteriaAdultos + 1
	CASO CONTRARIO:
		ESCRIBIR "Opción no válida."
FIN SEGÚN
FIN SI

totalVacunas <- totalVacunas + 1
FIN MIENTRAS


ESCRIBIR "--------- Resumen de la Jornada de Vacunación ---------"
ESCRIBIR "Fiebre Amarilla - Niños: ", fiebreAmarillaNinos, ", Adultos: ", fiebreAmarillaAdultos
ESCRIBIR "Varicela - Niños: ", varicelaNinos, ", Adultos: ", varicelaAdultos
ESCRIBIR "Rubeola - Niños: ", rubeolaNinos, ", Adultos: ", rubeolaAdultos
ESCRIBIR "Meningococo - Niños: ", meningococoNinos, ", Adultos: ", meningococoAdultos
ESCRIBIR "Influenza - Niños: ", influenzaNinos, ", Adultos: ", influenzaAdultos
ESCRIBIR "Sarampión - Niños: ", sarampionNinos, ", Adultos: ", sarampionAdultos
ESCRIBIR "Hepatitis A - Niños: ", hepatitisANinos, ", Adultos: ", hepatitisAAdultos
ESCRIBIR "Tétano - Niños: ", tetanoNinos, ", Adultos: ", tetanoAdultos
ESCRIBIR "Difteria - Niños: ", difteriaNinos, ", Adultos: ", difteriaAdultos
ESCRIBIR "Total vacunas aplicadas en la jornada: ", totalVacunas
ESCRIBIR "------------------------------------------------------"


FinAlgoritmo
