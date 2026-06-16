import mysql.connector
import numpy as np 
import matplotlib.pyplot as plt


mydb=mysql.connector.connect(host="localhost",user="root",password="Admin12345",database="cosmeticos")
mycursor=mydb.cursor()
mycursor.execute("select nombre, cantidad from productos where (cantidad>=20);")
result=mycursor.fetchall
nombre=[]
cantidad=[]
for i in mycursor:
    nombre.append(i[0])
    cantidad.append(i[1])
    print("Nombre=",nombre)
    print("Cantidad=",cantidad)
    plt.bar(nombre,cantidad,color=("yellow","pink"))
    plt.ylim(0,80)
    plt.xlabel("Productos mas vendidos ")
    plt.ylabel("Cantidad de Productos")
    plt.title("Mayor venta ")
    plt.show()