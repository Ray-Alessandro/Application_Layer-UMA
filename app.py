from flask import Flask,render_template, jsonify, request
from flask_mysqldb import MySQL
from config import config
from flask_cors import CORS  # Importa Flask-CORS

app = Flask(__name__)

conexion = MySQL(app) # Se crea el objeto de conexion a la base de datos
CORS(app)  # Habilita CORS para tu aplicación

@app.route('/')
def Index():
    cur = conexion.connection.cursor()
    cur.execute("SELECT * FROM Producto") # Selecciona todos los registros de la tabla Usuario
    data = cur.fetchall()  # Recupera todos los resultados de la consulta y los almacena en data
    data_productos = data

    cur.execute("SELECT * FROM Usuario")
    data = cur.fetchall()
    data_usuarios = data

    cur.execute("SELECT * FROM Tienda")
    data = cur.fetchall()
    data_tiendas = data

    cur.close()

    return render_template('table-users.html', matriz_usuarios = data_usuarios , matriz_productos = data_productos, matriz_tiendas = data_tiendas )

#----------------------------------------------------
#----------------------Products----------------------
#----------------------------------------------------

@app.route('/products', methods=['GET'])
def getProducts():
    try:
        cursor = conexion.connection.cursor()
        sql="SELECT * FROM Producto"
        cursor.execute(sql)
        data=cursor.fetchall()
        print(data)
        products = []
        for row in data:
            product = {'Producto_ID':row[0],'nombre':row[1],'descripcion':row[2],'precio':row[3],'imagen':row[4]}
            products.append(product)
        return jsonify({'products':products, 'message':'success'})
    except Exception as e:
        return jsonify({'message':'error'})

@app.route('/products/<id>', methods=['GET'])
def getProduct(id):
    try:
        cursor = conexion.connection.cursor()
        sql="SELECT *  FROM Producto WHERE Producto_ID = '{0}'".format(id)
        cursor.execute(sql)
        data=cursor.fetchone()
        if data != None:
            product = {'Producto_ID':data[0],'nombre':data[1],'descripcion':data[2],'precio':data[3],'imagen':data[4]}
            return jsonify({'product':product, 'message':'success'})
        else:
            return jsonify({'message':'product not found'})
    except Exception as e:
        return jsonify({'message':'error'})

@app.route('/products', methods=['POST'])
def createProduct():
    # print(request.json)
    try:
        #verificar si el codigo existe
        cursor = conexion.connection.cursor()
        sql="INSERT INTO Producto (Producto_ID, nombre, descripcion, precio, imagen) VALUES ('{0}','{1}','{2}', '{3}','{4}')".format(request.json['Producto_ID'],request.json['nombre'],request.json['descripcion'],request.json['precio'],request.json['imagen'])
        cursor.execute(sql)
        conexion.connection.commit() #confirma la transaccion de inser
        return jsonify({'message':'product registered'})
    except Exception as e:
        print("Error:", str(e)) 
        return jsonify({'message':'error'})

@app.route('/products/<id>', methods=['DELETE'])
def deleteProduct(id):
    try:
        #verificar si el codigo existe
        cursor = conexion.connection.cursor()
        sql="DELETE FROM Producto WHERE Producto_ID = '{0}'".format(id)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la transaccion de insert
        
        return jsonify({'message':'product deleted'})
    except Exception as e:
        return jsonify({'message':'error'})

@app.route('/products/<id>', methods=['PUT'])
def updateProduct(id):
    try:
        #verificar si el codigo existe
        cursor = conexion.connection.cursor()
        sql="UPDATE Producto SET nombre = '{0}', descripcion = '{1}', precio = '{2}', imagen = '{3}' WHERE Producto_ID = '{4}'".format(request.json['nombre'],request.json['descripcion'],request.json['precio'],request.json['imagen'],id)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la transaccion de insert

        return jsonify({'message':'product updated'})
    except Exception as e:
        return jsonify({'message':'error'})


        
#--------------------------------------------------
#----------------------Users-----------------------
#--------------------------------------------------,

@app.route('/users', methods=['GET'])
def getUsers():
    try:
        cursor = conexion.connection.cursor()
        sql="SELECT * FROM Usuario"
        cursor.execute(sql)
        data=cursor.fetchall()
        print(data)
        users = []
        for row in data:
            user = {'Usuario_ID':row[0],'Nombres':row[1],'Apellidos':row[2],'correo':row[3],'numero_telefono':row[4],'Credencial_Credencial_ID':row[5], 'Localidad_Localidad_ID':row[6]}
            users.append(user)
        return jsonify({'users':users, 'message':'success'})
    except Exception as e:
        return jsonify({'message':'error'})

@app.route('/users/<id>', methods=['GET'])
def getUser(id):
    try:
        cursor = conexion.connection.cursor()
        sql="SELECT * FROM Usuario WHERE Usuario_ID = '{0}'".format(id)
        cursor.execute(sql)
        data=cursor.fetchone()
        if data != None:
            user = {
                'Usuario_ID':data[0],
                'Nombres':data[1],
                'Apellidos':data[2],
                'correo':data[3],
                'numero_telefono':data[4],
                'Credencial_Credencial_ID':data[5],
                'Localidad_Localidad_ID':data[6]                
            }
            return jsonify({'user':user, 'message':'success'})
        else:
            return jsonify({'message':'user not found'})
    except Exception as e:
        return jsonify({'message':'error'})

@app.route('/users', methods=['POST'])
def createUser():
    # print(request.json)
    try:
        #verificar si el codigo existe
        cursor = conexion.connection.cursor()
        sql="INSERT INTO Usuario (Usuario_ID, Nombres, Apellidos, correo, numero_telefono, Credencial_Credencial_ID, Localidad_Localidad_ID) VALUES ('{0}','{1}','{2}', '{3}', '{4}', '{5}', '{6}')".format(request.json['Usuario_ID'],request.json['Nombres'],request.json['Apellidos'],request.json['correo'],request.json['numero_telefono'],request.json['Credencial_Credencial_ID'],request.json['Localidad_Localidad_ID'])
        cursor.execute(sql)
        conexion.connection.commit() #confirma la transaccion de inser
        return jsonify({'message':'user registered'})
    except Exception as e:
        print("Error:", str(e)) 
        return jsonify({'message':'error'})
    

@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    try:
        #verificar si el codigo existe
        cursor = conexion.connection.cursor()
        sql="DELETE FROM Usuario WHERE Usuario_ID = '{0}'".format(id)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la transaccion de insert

        return jsonify({'message':'user deleted'})
    except Exception as e:
        return jsonify({'message':'error'})

@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    try:
        cursor = conexion.connection.cursor()
        sql="UPDATE Usuario SET Nombres = '{0}', Apellidos = '{1}', correo = '{2}', numero_telefono = '{3}', Credencial_Credencial_ID = '{4}', Localidad_Localidad_ID = '{5}' WHERE Usuario_ID = '{6}'".format(request.json['Nombres'],request.json['Apellidos'],request.json['correo'],request.json['numero_telefono'],request.json['Credencial_Credencial_ID'],request.json['Localidad_Localidad_ID'],id)
        cursor.execute(sql)
        conexion.connection.commit() #confirma la transaccion de insert
        return jsonify({'message':'user updated'})
    except Exception as e:
        return jsonify({'message':'error'})



def page_not_found(error):
    return "<h1>Page not found</h1>", 404


if __name__ == '__main__':
    #accede a la configuracion de desarrollo
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run(debug = True)