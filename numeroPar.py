def main():
  
  numeros = int(input("¿Cuántos valores va a introducir? "))
  if numeros < 0:
      print("no es posible numeros menores que cero")
  else:
   
       pares = 0
  
  for i in range(1, numeros + 1):
          numero = int(input(f"Escriba el valor {i}: "))
          if numero % 2 == 0:
              pares += 1
              bool(numero == pares)
              True
              print(f"Ha escrito {pares} números pares") 
      
if __name__ == "__main__":
 main()