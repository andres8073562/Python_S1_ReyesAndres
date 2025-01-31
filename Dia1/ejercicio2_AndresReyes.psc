Algoritmo ControlDeVentasCafeteria

		
		DEFINIR totalEmpanadasTrigo COMO ENTERO 
		DEFINIR totalEmpanadasYuca COMO ENTERO 
		DEFINIR totalBunuelos COMO ENTERO 
		DEFINIR totalPapasRellenas COMO ENTERO 
		DEFINIR totalGaseosas COMO ENTERO 
		DEFINIR totalSpeedMax COMO ENTERO 
		DEFINIR opcion, cantidad, subtotal COMO ENTERO
		DEFINIR totalGeneral COMO ENTERO 
		
		totalEmpanadasTrigo <-0
		totalEmpanadasYuca<-0
		totalBunuelos<-0
		totalPapasRellenas<-0
		totalGaseosas<-0
		totalSpeedMax<-0
		totalGeneral<-0
		
		
		
		MIENTRAS VERDADERO HACER
			ESCRIBIR "Menú de productos:"
			ESCRIBIR "1. Empanadas de trigo con pollo ($3000)"
			ESCRIBIR "2. Empanadas de yuca con pollo y queso ($3000)"
			ESCRIBIR "3. Buñuelos ($2500)"
			ESCRIBIR "4. Papas rellenas ($4500)"
			ESCRIBIR "5. Gaseosa ($2000)"
			ESCRIBIR "6. SpeedMax ($2000)"
			ESCRIBIR "0. Finalizar y mostrar resumen de ventas"
			ESCRIBIR "Seleccione una opción:"
			LEER opcion
			
			SI opcion = 0 ENTONCES
				
				Escribir "SALIR"
			FIN SI
			
			
			ESCRIBIR "Ingrese la cantidad a comprar:"
			LEER cantidad
			
			
			SEGÚN opcion HACER
		CASO 1:
			subtotal <- cantidad * 3000
			totalEmpanadasTrigo <- totalEmpanadasTrigo + subtotal
		CASO 2:
			subtotal <- cantidad * 3000
			totalEmpanadasYuca <- totalEmpanadasYuca + subtotal
		CASO 3:
			subtotal <- cantidad * 2500
			totalBunuelos <- totalBunuelos + subtotal
		CASO 4:
			subtotal <- cantidad * 4500
			totalPapasRellenas <- totalPapasRellenas + subtotal
		CASO 5:
			subtotal <- cantidad * 2000
			totalGaseosas <- totalGaseosas + subtotal
		CASO 6:
			subtotal <- cantidad * 2000
			totalSpeedMax <- totalSpeedMax + subtotal
		CASO CONTRARIO:
			ESCRIBIR "Opción no válida."
	FIN SEGÚN
	
	
	SI opcion >= 1 Y opcion <= 6 ENTONCES
		ESCRIBIR "Subtotal a pagar por esta compra: $", subtotal
	FIN SI
FIN MIENTRAS


totalGeneral <- totalEmpanadasTrigo + totalEmpanadasYuca + totalBunuelos + totalPapasRellenas + totalGaseosas + totalSpeedMax
ESCRIBIR "Resumen del recaudo:"
ESCRIBIR "Empanadas de trigo con pollo: $", totalEmpanadasTrigo
ESCRIBIR "Empanadas de yuca con pollo y queso: $", totalEmpanadasYuca
ESCRIBIR "Buñuelos: $", totalBunuelos
ESCRIBIR "Papas rellenas: $", totalPapasRellenas
ESCRIBIR "Gaseosa: $", totalGaseosas
ESCRIBIR "SpeedMax: $", totalSpeedMax
ESCRIBIR "Total recaudado: $", totalGeneral


FinAlgoritmo
