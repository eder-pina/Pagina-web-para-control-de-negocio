from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)

#Rutas de la aplicación
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM Productos")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)

#Ruta para guardar usuarios en la bdd
@app.route('/user', methods=['POST'])
def addUser():
    preciop = request.form['preciop']
    nombre = request.form['nombre']
    cantidad = request.form['cantidad']
    descripcion = request.form['descripcion']

    if preciop and nombre and cantidad and descripcion:
        cursor = db.database.cursor()
        sql = "INSERT INTO Productos (preciop, nombre, cantidad, descripcion) VALUES (%s, %s, %s, %s)"
        data = (preciop, nombre, cantidad, descripcion)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM Productos WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    preciop = request.form['preciop']
    nombre = request.form['nombre']
    cantidad = request.form['cantidad']
    descripcion = request.form['descripcion']

    if preciop and nombre and cantidad and descripcion:
        cursor = db.database.cursor()
        sql = "UPDATE Productos SET preciop = %s, nombre = %s, cantidad = %s, descripcion = %s WHERE id = %s"
        data = (preciop, nombre, cantidad, descripcion, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)