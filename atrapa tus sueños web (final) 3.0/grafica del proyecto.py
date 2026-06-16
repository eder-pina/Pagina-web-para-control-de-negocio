import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

mydb= mysql.connector.connect (host="localhost", user="root", password="Admin12345", database="cosmeticos")
mycursor=mydb.cursor()
mycursor.execute ("select nombre, cantidad from Productos;")
result=mycursor.fetchall
nombre=[]
cantidad=[]
for i in mycursor:
 nombre.append (i[0])
 cantidad.append (i[1])
print ("Nombre=",nombre)
print ("cantidad=",cantidad)
plt.bar (nombre, cantidad, color=("pink","aquamarine","violet","plum","tan","orange"))
plt.ylim (1,50)
plt.xlabel ("nombres productos")
plt.ylabel("cantidad productos")
plt.title ("menor cantidad")
plt.show ()