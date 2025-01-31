
##correo

import re

def validar_email(email):
    # Validación simple para un correo electrónico
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$', email))

def validar_telefono(numero_telefono, codigo_pais):
    # Validación simple para teléfono según código de país
    if codigo_pais == 'US':
        return bool(re.match(r'^\+1\d{10}$', numero_telefono))  # Formato: +1 seguido de 10 dígitos
    elif codigo_pais == 'MX':
        return bool(re.match(r'^\+52\d{10}$', numero_telefono))  # Formato: +52 seguido de 10 dígitos
    return False

def validar_contraseña(contraseña):
    # Validación simple para contraseña (mínimo 8 caracteres, al menos un dígito y una letra)
    return bool(re.match(r'^(?=.*[a-zA-Z])(?=.*\d).{8,}$', contraseña))

def validar_datos(email, numero_telefono, codigo_pais, contraseña):
    return (email)
print("email_valido", validar_email(email))
print("telefono_valido", validar_telefono(numero_telefono, codigo_pais))
print("contraseña_valida", validar_contraseña(contraseña))

##desarrolado por Camilo Andres Suarez Fuentes TI 1097784213