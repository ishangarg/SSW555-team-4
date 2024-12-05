import unittest
import requests

class TestPostData(unittest.TestCase):
    def test_post_data(self):
        data = {
            "user_id": "   testMail@gmail.com  ",
            "contacts": [{
                "contact_name": " Jane Doe",
                "phone_number": " 222-234-5679   "
            }]
        }
        # Trigger POST request
        response = requests.post("http://localhost:5000/emergencyContacts", json=data)

        # Verify response status code is 200 
        self.assertEqual(response.status_code, 200)

         # Parse the response data
        response_data = response.json()
        res_message = "Contact added successfully"
        self.assertIn("message", response_data)
        self.assertEqual(response_data["message"], res_message)

if __name__ == "__main__":
    unittest.main()
