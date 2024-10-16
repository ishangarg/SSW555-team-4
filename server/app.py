from flask import Flask, jsonify, request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# connecting to mongoDB
client = MongoClient("mongodb://localhost:27017/")

# database and collection names:
db = client.sprinters
collection = db.conversations

def validate_conversations(data):
    err = []
    if not isinstance(data, dict):
        err.append("The data is not of type 'object'")
        return err
    if "user_id" not in data:
        err.append("'user_id' must be present")
    elif not isinstance(data.get("user_id"), str):
        err.append("'user_id' must be a string")
    if "messages" not in data:
       err.append("'messages' must be present")
    elif not isinstance(data.get("messages"), list):
        err.append("'messages' must be a list")
    else:
        for i, message in enumerate(data["messages"]):
            if "timestamp" not in message:
                err.append(f"'timestamp' must be present in 'messages[{i}]'")
            elif not isinstance(message.get("timestamp"), str):
                err.append(f"messages[{i}].timestamp must be a string")
            elif not validate_timestamp(message.get("timestamp")):
                err.append(f"messages[{i}].timestamp is not valid")
            if "query" not in message:
                err.append(f"'query' must be present in 'messages[{i}]'")
            elif not isinstance(message.get("query"), str):
                err.append(f"messages[{i}].query must be a string")
            if "response" not in message:
                err.append(f"'response' must be present in 'messages[{i}]'")
            elif not isinstance(message.get("response"), str):
                err.append(f"messages[{i}].response must be a string")
    return err

def validate_timestamp(timestamp):
    try:
        valid_timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False
    
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
    data = collection.find_one({"user_id": data.get("user_id")}, {"_id": 0})
    if data:
        return jsonify({"message": f"Data for the user id: {data.get("user_id")} already exists, kindly submit an update request"}), 400
        # return update_data()
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