Algoritmo sin_titulo

		DEFINIR num1, num2, num3 COMO ENTEROS
		
		
		ESCRIBIR "Ingrese el primer número positivo:"
		LEER num1
		ESCRIBIR "Ingrese el segundo número positivo:"
		LEER num2
		ESCRIBIR "Ingrese el tercer número positivo:"
		LEER num3
		
		
		SI num1 <= 0 O num2 <= 0 O num3 <= 0 ENTONCES
			ESCRIBIR "Todos los números deben ser positivos. Fin del programa."
        
    FIN SI
	
    
    mayor <- num1
    menor <- num1
	
    
    SI num2 > mayor ENTONCES
        mayor <- num2
    FIN SI
    SI num3 > mayor ENTONCES
        mayor <- num3
    FIN SI
	

    SI num2 < menor ENTONCES
        menor <- num2
    FIN SI
    SI num3 < menor ENTONCES
        menor <- num3
    FIN SI
	
    
    ESCRIBIR "El número mayor es:", mayor
    ESCRIBIR "El número menor es:", menor
FIN ALGORITMO


