import unittest
from flask import json
from app import app, collection
from pymongo.errors import ServerSelectionTimeoutError

class FlaskTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True

        try:
            collection.database.client.admin.command('ping')
        except ServerSelectionTimeoutError:
            raise RuntimeError("Could not connect to MongoDB. Ensure MongoDB is running.")

    def test_db_connection(self):
        try:
            collection.database.client.admin.command('ping') # Check if the MongoDB is there
            connection_success = True
        except ServerSelectionTimeoutError:
            connection_success = False

        self.assertTrue(connection_success, "Mongo connection failed.")

    def test_add_entry(self):
        data = {
            "user_id": "test_user_5",
            "messages": [
                {
                    "timestamp": "2024-10-15 12:00:00",
                    "query": "Hello, world!",
                    "response": "Hi! How can I help you?"
                }
            ]
        }

        response = self.app.post('/add', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200, "Failed to add conversation entry")
        response_json = json.loads(response.data)
        self.assertEqual(response_json["message"], "Data inserted!", "Data insertion message mismatch")

    def test_get_entry(self):
        """Test retrieving a conversation entry by user_id."""
        user_id = "test_user_1"

        response = self.app.get(f'/dataById?user_id={user_id}')
        self.assertEqual(response.status_code, 200, "Failed to retrieve conversation entry")

        response_json = json.loads(response.data)
        self.assertEqual(response_json["user_id"], user_id, "Retrieved user_id mismatch")
        self.assertEqual(len(response_json["messages"]), 1, "Number of messages mismatch")
        self.assertEqual(response_json["messages"][0]["query"], "Hello, world!", "Query mismatch in the messages")

if __name__ == '__main__':
    unittest.main()
