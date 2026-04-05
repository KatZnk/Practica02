
def cifrado(texto, desplazamiento):
    resultado = ""
    
    for char in texto:
        if char.isupper():
            nuevo_ascii = (ord(char) - 65 + desplazamiento) % 26 + 65
            resultado += chr(nuevo_ascii)
            
        elif char.islower():
            # Para minúsculas empezamos desde 97 (a=97)
            nuevo_ascii = (ord(char) - 97 + desplazamiento) % 26 + 97
            resultado += chr(nuevo_ascii)
            
        else:
            resultado += char
            
    return resultado