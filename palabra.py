def main(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(' ', '')
    cadena = len(palabra)
    if cadena % 2 == 0:
        izquierda = palabra[:cadena // 2]
        derecha = palabra[cadena // 2:]
    else:
        izquierda = palabra[:cadena // 2]
        derecha = palabra[cadena // 2 + 1:]
    
    return izquierda == derecha[::-1]


print(main('1001'))
print(main('claseSoftware'))

print()

print(main('1001'))
print(main('luzazul'))