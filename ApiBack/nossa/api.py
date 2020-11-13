from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps


#db_connect = create_engine('sqlite:///C:\\users\\NoteSam\\Documents\\__Danilo\\ApiPython\\ApiFront\\rest-api\\exemplo.db', echo=True)
db_connect = create_engine('postgresql://postgres:banco123@localhost:5432/Teste')
#db_connect = create_engine('sqlite:///exemplo.db')
app = Flask(__name__)
api = Api(app)


class users(Resource):
    @app.route('/users', methods=['GET'])
    def get():
        conn = db_connect.connect()
        query = conn.execute("select id, name, email from users order by id")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        print(result)
        return jsonify(result)

    @app.route('/users', methods=['POST'])
    def post():

        print(request.json)

        conn = db_connect.connect()
        id1 = request.json['id']
        name = request.json['name']
        email = request.json['email']

        
        print(id1)
        print(name)
        print(email)

        conn.execute("insert into users(name, email) values('{0}','{1}')".format(name, email))

        query = conn.execute('select * from users order by id desc limit 1')
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    @app.route('/users', methods=['PUT'])
    def put():

        print(request.json)

        conn = db_connect.connect()
        id1 = request.json['id']
        name = request.json['name']
        email = request.json['email']

        
        print(id1)
        print(name)
        print(email)


        conn.execute("update users set name ='" + str(name) +
                     "', email ='" + str(email) + "'  where id =%d " % int(id1))

        query = conn.execute("select * from users where id=%d " % int(id1))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

class usersById(Resource):
    def delete(self, id):

        print(request.json)

        conn = db_connect.connect()
        conn.execute("delete from users where id=%d " % int(id))
        #return {"status": "success"}

        query = conn.execute("select id, name, email from users order by id")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)          

    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("select * from users where id =%d " % int(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result) 


api.add_resource(users, '/users') 
api.add_resource(usersById, '/users/<id>')

if __name__ == '__main__':
    app.run()

