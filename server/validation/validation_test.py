import unittest
from validation import validate_contact, validate_conversations, validate_timestamp

class TestValidationFunctions(unittest.TestCase):

    def test_validate_conversations(self):
        data = {
            "user_id": "12345",
            "messages": [
                {
                    "query": "Hello",
                    "response": "Hi there!",
                }
            ]
        }
        self.assertEqual(validate_conversations(data), [])

        data = {
            "user_id": 12345, 
            "messages": [
                {
                    "query": "Hello",
                    "response": "Hi there!",
                }
            ]
        }
        self.assertIn("'user_id' must be a string", validate_conversations(data))

        data = {
            "user_id": "12345"
        }
        self.assertIn("'messages' must be present", validate_conversations(data))

        data = {
            "user_id": "12345",
            "messages": "Not a list"
        }
        self.assertIn("'messages' must be a list", validate_conversations(data))

        data = {
            "user_id": "12345",
            "messages": [
                {
                    "response": "Hi there!"
                }
            ]
        }
        self.assertIn("'query' must be present in messages[0]", validate_conversations(data))

        data = {
            "user_id": "12345",
            "messages": [
                {
                    "query": "Hello"
                }
            ]
        }
        self.assertIn("'response' must be present in messages[0]", validate_conversations(data))

    def test_validate_contact(self):
        data = {
            "user_id": "12345",
            "contacts": [
                {
                    "contact_name": "Alice",
                    "phone_number": "+14155552671"
                }
            ]
        }
        self.assertEqual(validate_contact(data), [])

        data = {
            "user_id": 12345,  
            "contacts": [
                {
                    "contact_name": "Alice",
                    "phone_number": "+14155552671"
                }
            ]
        }
        self.assertIn("'user_id' must be a string", validate_contact(data))

        data = {
            "user_id": "12345"
        }
        self.assertIn("'contacts' must be present", validate_contact(data))

        data = {
            "user_id": "12345",
            "contacts": "Not a list"
        }
        self.assertIn("'contacts' must be a list", validate_contact(data))

        data = {
            "user_id": "12345",
            "contacts": [
                {
                    "phone_number": "+14155552671"
                }
            ]
        }
        self.assertIn("'contact_name' must be present", validate_contact(data))

        data = {
            "user_id": "12345",
            "contacts": [
                {
                    "contact_name": "Alice",
                    "phone_number": "12345"  
                }
            ]
        }
        self.assertIn("The 'phone_number': 12345 is invalid", validate_contact(data))

        data = {
            "user_id": "12345",
            "contacts": [
                {
                    "contact_name": " Alice ",
                    "phone_number": "+14155552671"
                }
            ]
        }
        validate_contact(data)
        self.assertEqual(data["contacts"][0]["contact_name"], "Alice") 

if __name__ == "__main__":
    unittest.main()
