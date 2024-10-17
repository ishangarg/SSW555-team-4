import unittest
from errorhandling import VoiceAssistant  

class TestVoiceAssistant(unittest.TestCase):

    def setUp(self):
        self.assistant = VoiceAssistant(valid_commands=["play music", "turn off lights", "set alarm", "talk to me"])

    def test_error_to_understand_conversation(self):
        result = self.assistant.process_command("")
        self.assertEqual(result, "Error: I couldn't understand what you said. Can you please clarify?")

    def test_error_generating_response(self):
        result = self.assistant.process_command("open door")
        self.assertEqual(result, "Error: Something went wrong while generating a response. Try asking something else.")

    def test_no_response_due_to_error(self):
        result = self.assistant.handle_system_error()
        self.assertEqual(result, "Error: There was an issue. Please expect a delayed response or try again later.")

if __name__ == '__main__':
    unittest.main()
