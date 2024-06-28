def  separar_por_caracter(cadena):
    caracteres = []
    for caracter in cadena:
        caracteres.append(caracter)
    return caracteres
    
    
cadena_usuario = input("ingrese una cadena de texto: ")

caracteres_separados = separar_por_caracter(cadena_usuario)
print("cadena separada por caracteres: ", caracteres_separados)