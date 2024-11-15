import unittest
from unittest.mock import patch, mock_open
import sys
import os
import io

import text2speech  # Import the text2speech module

class TestTextToSpeechScript(unittest.TestCase):
    def setUp(self):
        self.test_file_name = 'test_output.mp3'
        self.test_text_content = "This is a sample text for testing."
        self.input_file_name = 'fake_file.txt'

        # Remove any test files if they already exist
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)
        if os.path.exists(self.input_file_name):
            os.remove(self.input_file_name)

    def tearDown(self):
        # Clean up created files after tests
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)
        if os.path.exists(self.input_file_name):
            os.remove(self.input_file_name)

    @patch('sys.argv', ['text2speech.py'])
    def test_no_arguments(self):
        """
        Test that text2speech exits with code 1 and prints usage when no arguments are provided.
        """
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout, \
                self.assertRaises(SystemExit) as cm:
            text2speech.main()
        output = mock_stdout.getvalue()
        self.assertIn("Usage:", output)
        self.assertEqual(cm.exception.code, 1)

    @patch('sys.argv', ['text2speech.py', 'non_existing_file.txt'])
    def test_file_not_found(self):
        """
        Test that text2speech exits with code 1 if the file is not found.
        """
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout, \
                self.assertRaises(SystemExit) as cm:
            text2speech.main()
        output = mock_stdout.getvalue()
        self.assertIn("File not found:", output)
        self.assertEqual(cm.exception.code, 1)

    @patch('builtins.open', new_callable=mock_open, read_data="This is a sample text for testing.")
    @patch('sys.argv', ['text2speech.py', 'fake_file.txt', 'test_output.mp3'])
    def test_text_to_speech_conversion(self, mock_file):
        """
        Test that the script reads the file and calls text_to_speech with the correct parameters.
        """
        with patch.object(text2speech, 'text_to_speech', return_value=None) as mock_tts:
            text2speech.main()
            mock_tts.assert_called_once_with(self.test_text_content, 'test_output.mp3')

    @patch('builtins.open', new_callable=mock_open, read_data="This is a sample text for testing.")
    @patch('sys.argv', ['text2speech.py', 'fake_file.txt'])
    def test_default_output_filename(self, mock_file):
        """
        Test that the default output filename 'output.mp3' is used when no output filename is provided.
        """
        with patch.object(text2speech, 'text_to_speech', return_value=None) as mock_tts:
            text2speech.main()
            mock_tts.assert_called_once_with(self.test_text_content, 'output.mp3')

    @patch('sys.argv', ['text2speech.py', 'fake_file.txt', 'test_output.mp3'])
    def test_output_file_creation(self):
        """
        Test that an output file is actually created.
        """
        # Write the input content to a real file
        with open(self.input_file_name, 'w', encoding='utf-8') as file:
            file.write(self.test_text_content)

        text2speech.main()
        self.assertTrue(os.path.exists(self.test_file_name), f"{self.test_file_name} was not created.")


if __name__ == '__main__':
    unittest.main()
