<<<<<<< HEAD
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

records = {
    'Dunah': 'cat',
    'Hector': 'dog',
    'AP': 'human'
}

class LovelyCreature(Resource):
    def get(self, name):
        if name in records:
            return {name: records[name]}, 200
        return {'error': 'Creature not found'}, 404
    
    def post(self, name):
        data = request.get_json()
        if not data or 'type' not in data:
            return {'error': 'Missing "type" in JSON payload'}, 400
        
        creature_type = data['type']
        records[name] = creature_type
        return{name: records[name]}, 201

api.add_resource(LovelyCreature, '/creature/<string:name>')

@app.route('/')
def home():
    return "<h1>Welcome to the Creature API</h1><p>Use /creature/&lt;name&gt; to get data.</p>", 200

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

records = {
    'Dunah': 'cat',
    'Hector': 'dog',
    'AP': 'human'
}

class LovelyCreature(Resource):
    def get(self, name):
        if name in records:
            return {name: records[name]}, 200
            # 200 means ok
        return {'error': 'Creature not found'}, 404
    
    def post(self, name):
        # Get payload
        data = request.get_json()
        
        if not data:
            return {"message": "No data provided"}, 400
        
        records.update(data)  # Add new entry
        return {"message": "Record updated", "data": records}, 201 #201 means created
    
api.add_resource(LovelyCreature, '/creature/<string:name>')

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 57c5c2c (Update app)
