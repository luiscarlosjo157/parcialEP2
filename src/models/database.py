from src.config.db import mysql

class DatabaseModel():
    def listarDatabase(self):
        cursor = mysql.get_db().cursor()
        cursor.execute('show databases')
        schemas = cursor.fetchall()
        cursor.close()
        return schemas

    def crearDatabase(serlf,prueba):
        cursor = mysql.get_db().cursor()
        cursor.execute('CREATE DATABASE'+ prueba)
        mysql.get_db().commit()
        cursor.close()
    
    def listarTablas(self):
        cursor = mysql.get_db().cursor()
        cursor.execute('DESCRIBE flask_mvc')
        database = cursor.fetchall()
        cursor.close()
        return database
    """select
table_schema,
table_name,
column_name,
data_type
from
information_schema.columns
where
table_schema = 'facturacion'
order
by table_name, table_name;*/"""
   
   