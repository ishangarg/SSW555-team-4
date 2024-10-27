from flask import Flask, jsonify, request
from pymongo import MongoClient
from datetime import datetime
from validation.validation import validate_conversations, validate_timestamp
from bson import ObjectId

app = Flask(__name__)

# connecting to mongoDB
client = MongoClient("mongodb://localhost:27017/")

# database and collection names:
db = client.sprinters
collection = db.conversations
    
@app.route('/')
def home():
    return "Welcome!"

@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    val_err = validate_conversations(data)
    if val_err:
        print("Validation failed with the following errors:")
        final_error_message = ""
        for err in val_err:
            final_error_message = final_error_message + err + "\n"
        return jsonify({"message": final_error_message}), 400
    
    # Check if the user_id already exists
    existing_data = collection.find_one({"user_id": data.get("user_id")}, {"_id": 0})
    if existing_data:
        for message in data['messages']:
            message['_id'] = ObjectId()
        
            collection.update_one(
                {"user_id": data.get("user_id")},
                {"$push": {"messages": {"$each": data["messages"]}}}
            )
        return jsonify({"message": "Messages appended to existing user data"}), 200
    
    for i, message in enumerate(data['messages']):
        message['_id'] = ObjectId()
    collection.insert_one(data)  
    
    return jsonify({"message": "Data inserted!"}), 200

@app.route('/update', methods=['PUT'])
def update_data():
    data = request.json
    val_err = validate_conversations(data)
    if val_err:
        print("Validation failed with the following errors:")
        final_error_message = ""
        for err in val_err:
            final_error_message = final_error_message + err + "\n" 
        return jsonify({"message": final_error_message}), 400
    old_data = collection.find_one({"user_id": data.get("user_id")})
    if not old_data:
        msg = f"No conversations found for the user with id: {data.user_id}"
        return jsonify({"message": msg}), 400
    all_messages = old_data.get("messages", []) + data.get("messages", [])
    print(all_messages)
    data["messages"] = all_messages
    collection.find_one_and_update(
        {"user_id": data.get("user_id")},
        {"$set": data}
    )
    return jsonify({"message": "Data updated!"}), 200

@app.route('/data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data), 200

@app.route('/dataById', methods=['GET'])
def get_data_by_id():
    user_id = request.args.get('user_id', 'undefined')
    data = collection.find_one({"user_id": user_id}, {"_id": 0})
    if not data:
        return jsonify({"message": f"Data with the user id: {user_id} not found"}), 404
    print(data)
    return data, 200

if __name__ == "__main__":
    app.run(debug=True)