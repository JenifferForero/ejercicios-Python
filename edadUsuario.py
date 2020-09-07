import datetime
 
def edad(naci):
    hoy = datetime.date.today()
    if hoy < naci:
        print ('fecha de nacimiento')
    else:
        ano = naci.year
        mes = naci.month
        dia = naci.day
 
        fecha = naci
        edad = 0
        respuesta= edad+(2070-ano)
        while fecha < hoy:
            edad += 1
            fecha = datetime.date(ano+edad, mes, dia)
 
        print ('Mi edad es: %s' % (respuesta))
 
edad(datetime.date(2000, 3, 15))

    
  


