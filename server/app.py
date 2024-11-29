from flask import Flask, jsonify, request
from pymongo import MongoClient
from datetime import datetime
from validation.validation import validate_conversations, validate_timestamp, validate_contact
from bson import ObjectId
import phonenumbers
from flask_cors import CORS
import speech_recognition as sr
from pydub import AudioSegment
import os
from chatgpt.ai import chatgpt
from chatgpt.gemini_API import transcribe_and_get_mood 
import json

app = Flask(__name__)

CORS(app, resources={r"/*": {
    "origins": "*",
    "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    "allow_headers": ["Content-Type", "Authorization", "X-Requested-With"]
}})

# connecting to mongoDB
client = MongoClient("mongodb://localhost:27017/")
# ai = AI(key='')

# database and collection names:
db = client.sprinters
collection = db.conversations
ec_collection = db.contacts

def convert_audio_to_wav(input_file):
    file_ext = os.path.splitext(input_file)[1].lower()
    if file_ext != '.wav':
        sound = AudioSegment.from_file(input_file)
        input_file = os.path.splitext(input_file)[0] + '.wav'
        sound.export(input_file, format='wav')
    return input_file

def transcribe_audio(input_file):
    r = sr.Recognizer()
    with sr.AudioFile(input_file) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results; {e}"

@app.route('/')
def home():
    return "Welcome!"

@app.route('/add', methods=['POST', 'OPTIONS'])
def add_data():
    data = request.json
    val_err = validate_conversations(data)
    if val_err:
        print("Validation failed with the following errors:")
        final_error_message = ""
        for err in val_err:
            final_error_message = final_error_message + err + "\n"
        return jsonify({"message": final_error_message}), 400
    
    for i, message in enumerate(data['messages']):
        message['_id'] = ObjectId()
        message['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Check if the user_id already exists
    existing_data = collection.find_one({"user_id": data.get("user_id")}, {"_id": 0})
    if existing_data:
        for message in data['messages']:
            # message['_id'] = ObjectId()
        
            collection.update_one(
                {"user_id": data.get("user_id")},
                {"$push": {"messages": {"$each": data["messages"]}}}
            )
        return jsonify({"message": "Messages appended to existing user data"}), 200
    
    
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
    for i, message in enumerate(data['messages']):
        message['_id'] = ObjectId()
        message['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
    data = list(collection.find({}, {"_id": 0, 'messages._id': 0}))
    return jsonify(data), 200

@app.route('/dataById', methods=['GET'])
def get_data_by_id():
    user_id = request.args.get('user_id')
    if user_id is None:
        return jsonify({"message": "'user_id' not provided"}), 400
    data = collection.find_one({"user_id": user_id}, {"_id": 0, 'messages._id': 0})
    if not data:
        return jsonify({"message": f"Data with the user id: {user_id} not found"}), 404
    print(data)
    return data, 200

@app.route('/emergencyContacts', methods=['POST'])
def add_emergency_contacts():
    data = request.json
    val_err = validate_contact(data)
    data["user_id"] = data["user_id"].strip()
    if val_err:
        print("Validation failed with the following errors:")
        final_error_message = ""
        for err in val_err:
            final_error_message = final_error_message + err + "\n" 
        return jsonify({"message": final_error_message}), 400
    for i, contact in enumerate(data['contacts']):
        contact['_id'] = ObjectId()
    # if contacts are already present for a user, then the contact will be appended to the existing list
    old_data = ec_collection.find_one({"user_id": data.get("user_id")})
    if not old_data:
        ec_collection.insert_one(data)
    else:
        all_contacts = old_data.get("contacts", []) + data.get("contacts", [])
        data["contacts"] = all_contacts
        ec_collection.find_one_and_update({"user_id": data.get("user_id")},{"$set": data})
    return jsonify({"message": "Contact added successfully"}), 200

@app.route('/emergencyContacts', methods=['GET'])
def get_emergency_contacts():
    user_id = request.args.get('user_id')
    if user_id is None:
        return jsonify({"message": "'user_id' not provided"}), 400
    data = ec_collection.find_one({"user_id": user_id}, {"_id": 0, 'contacts._id': 0})
    if not data:
        return jsonify({"message": f"Data with the user id: {user_id} not found"}), 404
    print(data)
    return data, 200

@app.route('/transcribe_audio', methods=['POST'])
def transcribe_audio_route():
    if 'audio' not in request.files:
        return jsonify({"message": "No audio file provided"}), 400
    
    audio_file = request.files['audio']
    input_path = os.path.join("/tmp", audio_file.filename)
    audio_file.save(input_path)


    
    # Convert audio to wav if necessary
    # wav_file = convert_audio_to_wav(input_path)

    transcription_mood = transcribe_and_get_mood(input_path)
    print(transcription_mood)
    answer = chatgpt(transcription_mood['transcript'])
    
    # Transcribe the audio
    # transcription = transcribe_audio(wav_file)
    
    # Clean up the temporary file
    os.remove(input_path)
    
    return jsonify({"transcription": transcription_mood['transcript'], 'mood': transcription_mood['emotion'], 'score': transcription_mood['sentiment_score'], 'answer': answer}), 200

if __name__ == "__main__":
    app.run(debug=True)