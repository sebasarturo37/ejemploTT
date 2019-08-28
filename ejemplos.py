#variables
# int, str, bool, float


"""
def persona(nombre, apellido, edad, estudia):

    print (f"hola", nombre, f"su apellido es: ", apellido, f"Su edad es: ", edad, f"Usted estudia en: ", estudia)

nombre = input("Digite su nombre: ")
apellido = input("Digite su apellido: ")
edad = input("Digite edad: ")
estudia = input("Donde estudia?: ")

persona(nombre, apellido, edad, estudia)
"""

"""
def suma (a, b):

    res = a + b

    print("El resultado de la suma es: ", res)

a = int(input("Digite numero A:"))
b = int(input("Digite numero B: "))

suma(a,b)

def resta (a, b):

    resu = a - b

    print("El resultado de la resta es: ", resu)

resta(a, b)

def div (a, b):

    resul = a / b

    print("El resultado de la division es: ", resul)

div(a, b)

def multi (a, b):

    result = a * b

    print("El resultado de la multiplicacion es: ", result)
"""
#multi(a, b)

print(".: Bienvenido Estudiante, por favor digite sus notas :.")

def prome(a, b, c, d):

    acum = a + b + c + d

    promedio = acum / 4 

    print("El promedio es: ", promedio)

#Condición para emitir mensaje según nota.
    if promedio < 2.9:
        print("Lástima, usted ha reprobado el curso.!")
    elif promedio >= 3.0 :
        print("Felicitaciones, usted aprobó el curso.!")

a = float(input("Digite nota 1:"))
b = float(input("Digite nota 2:"))
c = float(input("Digite nota 3:"))
d = float(input("Digite nota 4:"))

prome(a, b, c, d)

