from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
import os
from bson.objectid import ObjectId
import json

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

mongodb_host = os.environ.get('MONGO_HOST', 'localhost')
mongodb_port = int(os.environ.get('MONGO_PORT', '27017'))
client = MongoClient(mongodb_host, mongodb_port)

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

@app.route('/rental', methods=['POST', 'GET'])
def rental():
    db = client.rental
    if request.method == 'GET':
        person = db.person.find()
        result = []
        # return ok(person, "")

        for i in person:
            result.append(i)

        return JSONEncoder().encode(result)
'''
        return result

        return render_template('home.html', my_string="Welcome Home!", title="Home", data=result)
elif:
        return

@app.route('/rental/<id>', methods=['PUT', 'GET', 'DELETE'])
def rentalDetails(id):
    if :
        return
    elif:
        return
    elif:
        return
'''

@app.route('/rental/<id>', methods=['PUT', 'DELETE'])
def rentalDetail(id):
    db = client.rental
    if request.method == 'PUT':
        insert=request.get_json()
        #person = db.person.find({"_id":ObjectId(id)})
        #result = []
        #for i in person:
        #    result.append(i)

        #name=request.values.get("name")
        #address=request.values.get("address")
        #id=request.values.get("id")
        #db = client.rental

        db.person.update(
            {"_id":ObjectId(id)},
            {'$set':{
            "name" : insert['name'],
            "address" : insert['address']
            }
        })

        return JSONEncoder().encode(db.person.find_one(ObjectId(id)))

    if request.method == 'DELETE':
        db.person.remove({"_id":ObjectId(id)})

        return {"result" : "ok"}

if __name__ == '__main__':
    app.run(debug=True)
