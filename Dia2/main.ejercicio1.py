#####//////// grados celcius a farenhait



def converts  (n):
 Fah= 3*9/5*n +32
 return Fah

def faheraint (k):
 cell=k-32 * 1.8
 return cell


while True:
    try:
      
      elciusfarenhait=int(input("si quieres converir grados celcius a farenhait, coloca 1"))
      if elciusfarenhait in (1,2):
        break
      else:
        print("por favor ingrese 1 para converir grados celcius a fahrenhait o 2 para fahrenhait a celcius")
    except ValueError:
      print("Error: solo se puede ingresar numeros")

      if elciusfarenhait==1:
        k=int(input("dame los grados celcius para convertirlos a fahrenhait"))
      print("Esto son ",converts(elciusfarenhait), "grados fahrenhait" )
    if elciusfarenhait==2:
      klgradosfarenhait=int(input("Dame los grados fanherait que quiere convertir a celcius"))
      print("Esto son", faheraint(klgradosfarenhait),"grados celcius")

#/////  Desarrollado por Andres Reyes T.i 1097100508





