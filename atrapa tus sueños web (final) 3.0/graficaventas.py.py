import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

mybd=mysql.connector.connect(host="localhost",user="root",password ="Admin12345",database="cosmeticos" )
mycursor=mybd.cursor()
mycursor.execute("select fecha ,cantidad as total from ventas")
result=mycursor.fetchall

cantidad=[]
fecha=[]

for i in mycursor:
    
    cantidad.append(i[0])
    fecha.append(i[1])


print("Cantidad=",cantidad)
print("Fecha=",fecha)

plt.bar(cantidad,fecha,color=("pink","blue","orange","red"))
plt.ylim(0,3000)
plt.ylabel("Nombre de cosmeticos")
plt.ylabel("Cantidad de cosmeticos")
plt.ylabel("fecha de ventas")
plt.title ("grafica de fechas ventas")
plt.show()







