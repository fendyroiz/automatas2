#Primera parte de la actividad, pedimos al usuario una cadena de caracteres
# que sera comparado su contenido en el abecedario creado, para validar si hacen macht los caracteres
#
#1.-Primer paso, leer el abecedario de la ruta de recursos
#2.-Segundo paso separar los caracteres de la cadena dada por el usuario
#3.-Tercer paso, creamos una pequena validacion con la cadena de caracteres y el abecedario, donde 
#   Lo anadimos a un array de invalidos si el caracter no esta en el abecedario 
#4._Cuarto paso, Imprimimos los caracteres separados
#


def leer(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        abecedario = archivo.read().strip()
    return abecedario

def separar(cadena):
    caracteres = []
    for caracter in cadena:
        caracteres.append(caracter)
    return caracteres

def validar(cadena, abecedario):
    caracteres_invalidos = []
    for caracter in cadena:
        if caracter not in abecedario:
            caracteres_invalidos.append(caracter)
    return caracteres_invalidos

abecedario = leer('Recursos/abecedario.txt')
cadena = input("Ingrese una cadena de texto: ")


caracteres_separados = separar(cadena)
print("Cadena separada por caracteres:", caracteres_separados)


caracteres_invalidos = validar(cadena, abecedario)

if caracteres_invalidos:
    print("Se encontraron caracteres inválidos en la cadena:", caracteres_invalidos)
else:
    print("Todos los caracteres de la cadena son válidos.")
