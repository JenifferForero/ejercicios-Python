import random

intentos=0

print('Introduzca su nombre por favor')
nombre = input()

numero=random.randint(1,1000)
print('Bueno, '+nombre+', piensa un número entre 1 y 1000.')

while intentos<10:
    print ('Tienes 10 intentos')
    adivina=input()
    adivina=int(adivina)

    intentos=intentos+1
   
    if adivina<numero:
        print ('¡muy pequeño!')

    if adivina>numero:
        print('¡muy grande!')

    if adivina==numero:
        break

if adivina==numero:
    intentos=str(intentos)
    print('BIEN! '+nombre+', Adivino el numero en: '+intentos+' intentos :).')

if adivina!=numero:
    numero=str(numero)
    print('¡rayos '+nombre+' ! ese no era, el numero era: '+numero)