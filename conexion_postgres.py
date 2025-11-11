#scrip de py para conectar con una  DB postgresql
import psycopg2

try:
    conexion=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='postgres1234',
        database='clientes_db'
    )
    print("Conexion exitosa")
    cursor=conexion.cursor()
    cursor.execute("SELECT version()")  #para ver la version y probar la conexion
    row=cursor.fetchone()
    print(row)
    cursor.execute("SELECT * FROM clientes_table")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
finally:
    conexion.close()
    print("Conexion finalizada!")
