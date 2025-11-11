from tkinter import *
from tkinter import messagebox
import psycopg2
import os


try:
    miConexion=psycopg2.connect(
    host='localhost',
    user='postgres',
    password='postgres1234',
    database='dante_db'
    )
    print("Conexion exitosa")
    miCursor=miConexion.cursor()
    miCursor.execute('''
        INSERT INTO user_table (NOMBRE, APELLIDO, TELEFONO) VALUES ('adri', 'olme', 12354678); 
    ''')
    miConexion.commit()
except Exception as ex:
        print(ex)
finally:
    miConexion.close()
    print("Conexion finalizada!")



