from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///projeto.db')
app = Flask(__name__)
api = Api(app)


class Cars(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from carro")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        cor = request.json['cor']
        placa = request.json['placa']
        ano = request.json['ano']
        modelo = request.json['modelo']



        conn.execute(
            "insert into carro values(null, '{0}','{1}','{2}','{3}')".format(cor, placa, ano, modelo))

        query = conn.execute('select * from carro order by id desc limit 1')
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return result[0]['id'], 201

api.add_resource(Cars, '/cars', '/cars/') 

if __name__ == '__main__':
    app.run()
