# ETAPAS:
# Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.
while True:
     try:
       edad = int(input("Cual es su edad\n"))
       if edad >= 18:
        print("puede ingresar")
        break
       else:
        print("Debe ser mayor de edad")
    
     except:
      print("solo valor numerico")

# # Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
# User1: pedro   	Contraseña1: 1234
# User2: angel		Contraseña2: a4s1
User1 = "pedro"   	
Contrasena1 ="1234"
User2 = "angel"		
Contrasena2 = "a4s1"

usiario = input("ingrese su usuario\n")
passwd = input("ingrese contraseña\n")

if usiario == User1 and passwd == Contrasena1:
    print(f"bienvenido {usiario}")
elif usiario == User2 and passwd == Contrasena2:
    print(f"bienvenido {usiario}")
else:
    print("Usuario no encontrado")
# Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación), finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0.


try:
    nota1 = float(input("ingrese su nota 1\n"))
    nota2 = float(input("ingrese su nota 2\n"))
    nota3 = float(input("ingrese su nota 3\n"))
    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    if promedio >= 4 and promedio <= 7:
        print(f"Aprobado con: {promedio}")
    else:
        print(f"reprobaste con {promedio}")

except:
    print("Solo valores numericos")





































