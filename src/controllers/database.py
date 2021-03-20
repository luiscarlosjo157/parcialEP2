from flask import render_template, request, redirect, url_for, jsonify
from src import app
from src.models.database import DatabaseModel

@app.route('/database', methods=['GET'])
def listarDatabase():
    databaseModel = DatabaseModel()
    database = databaseModel.listarDatabase()
    return jsonify({"database":database})

@app.route("/createDatabase", methods=["POST"])
def createDatabase():
    databaseModel = DatabaseModel()
    request_data = request.get_json()
    prueba = request.json['prueba']
    databaseModel.crearDatabase(prueba)
    return 'database_creada'

@app.route('/listarTables', methods=['GET'])
def listarTables():
    databaseModel = DatabaseModel()
    lisatartables = databaseModel.listarTablas()
    return jsonify({"lisatartables":lisatartables})


