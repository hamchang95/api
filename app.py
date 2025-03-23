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
