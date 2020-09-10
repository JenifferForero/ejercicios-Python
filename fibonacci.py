lista=[0,1]
for i in range(3,21):
  lista.append(lista[len(lista)-1]+lista[len(lista)-2])
print(list(lista))