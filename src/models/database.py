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

   
   