input("Ingrese el nombre de la ciudad que desea calcular el promedio de su temperatura")
dia_semana=1#creo un contador para el ciclo while
list_temp=[]#creo una lista para almacenar las temperaturas
while dia_semana<8:
  temp=float(input('Temperatura dia'+str(dia_semana)+' : '))#pedimos la temperatura de los dias durante el ciclo while
  list_temp.append(temp)#vamos almacenando las temperaturas en la lista creada al principio
  dia_semana+=1#aumentamos contador
suma=0
for i in list_temp:#recorremos la lista
  suma+=i#sumamos las temperaturas de cada día
  media=suma/7#hallamos media
  media=round(media,2)#redondeamos a 2 decimales
print('La temperatura media de la semana es de '+str(media))#imprimimos mensaje de