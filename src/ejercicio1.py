def res(text):
    lineas = text.splitlines()
    total_lineas = len(lineas)
    palabras = len(text.split())
    promedio = palabras/total_lineas
    print (f"Total de lineas: {total_lineas}")
    print(f"Total de palabras: {palabras}")
    print(f"Promedio de palabras por linea: {promedio:.1f}")
    print(f"Lineas por encima del promedio: ")

    for elem in lineas:
        cant = len(elem.split())
        if cant > promedio:
            print(f'- "{elem}  " ({cant} palabras)')