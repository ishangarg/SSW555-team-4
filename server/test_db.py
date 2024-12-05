

import unittest
import requests

class TestPostData(unittest.TestCase):
    #TEST CASE TO VALIDATE INVALID FIELDS:
    def test_post_data(self):
        data = {
            "user_id": "   testMail@gmail.com  ",
            "contacts": [{
                "contact_name": " Jane Doe ",
                "dummy": " 201-234-5679   "
            }]
        }
        # Trigger POST request
        response = requests.post("http://localhost:5000/emergencyContacts", json=data)
        # Verify response status code is 400 
        self.assertEqual(response.status_code, 400)
         # Parse the response data
        response_data = response.json()
        json_response = {
            "message": "'phone_number' must be present\n"
        }
        self.assertIn("message", response_data)
        self.assertEqual(response_data["message"], json_response["message"])

if __name__ == "__main__":
    unittest.main()
