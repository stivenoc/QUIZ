lista1 =[35,0,45,21]

lista2 =[0.05,0.10,0.20,0.06]

resultado=[]

for i in range(len(lista1)):
    multiplicacion = lista1[i] * lista2[i]
    resultado.append(multiplicacion)
print(resultado)
suma = 0
for k in resultado:
    
    suma += k

print("suma de los valores de la lista para sacar el promedio", suma)

