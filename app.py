from flask import Flask,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '20.118.187.218'
app.config['MYSQL_USER'] = 'admin01'
app.config['MYSQL_PASSWORD'] = 'admin01'
app.config['MYSQL_DB'] = 'UMA_DB'
mySQL = MySQL(app)

@app.route('/')
def Index():
    cur = mySQL.connection.cursor()
    cur.execute("SELECT * FROM Producto")  # Selecciona todos los registros de la tabla Usuario
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


if __name__ == '__main__':  
    app.run(debug = True)