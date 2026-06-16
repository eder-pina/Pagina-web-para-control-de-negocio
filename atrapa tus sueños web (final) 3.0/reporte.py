import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

mybd=mysql.connector.connect(host="localhost",user="root", password="Admin12345",database="cosmeticos")
mycursor=mybd.cursor()
mycursor.execute("select  nombre, preciop*cantidad as total from Productos;")
result=mycursor.fetchall
nombre=[]
cantidad=[]
for i in mycursor:
    nombre.append(i[0])
    cantidad.append(i[1])
print("Nombre=",nombre)
print("Cantidad=",cantidad)
plt.bar(nombre,cantidad,color=("pink", "yellow","blue","orange"))
plt.ylim(0,3000)
plt.xlabel("nombres Cosmeticos")
plt.ylabel("Cantidad de cosmeticos")
plt.title("Graficas de costos productos")
plt.show()
