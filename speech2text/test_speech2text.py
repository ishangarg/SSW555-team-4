# test_speech2text.py

import unittest
from unittest.mock import patch, MagicMock
import speech2text
import os
import requests
from pydub import AudioSegment
import speech_recognition as sr

class TestSpeech2Text(unittest.TestCase):

    @patch('speech2text.AudioSegment')
    def test_convert_audio_to_wav_mp3(self, mock_audio_segment):
        # Mock the input and output
        input_file = 'test_audio.mp3'
        expected_output = 'test_audio.wav'

        # Mock the from_file and export methods
        mock_sound = MagicMock()
        mock_audio_segment.from_file.return_value = mock_sound

        output_file = speech2text.convert_audio_to_wav(input_file)

        mock_audio_segment.from_file.assert_called_with(input_file)
        mock_sound.export.assert_called_with(expected_output, format='wav')
        self.assertEqual(output_file, expected_output)

    def test_convert_audio_to_wav_wav(self):
        # No conversion should happen if the file is already a WAV
        input_file = 'test_audio.wav'
        output_file = speech2text.convert_audio_to_wav(input_file)
        self.assertEqual(output_file, input_file)

    @patch('speech2text.sr.AudioFile')
    @patch('speech2text.sr.Recognizer')
    def test_transcribe_audio_success(self, mock_recognizer_class, mock_audio_file_class):
        # Mock recognizer and audio file
        mock_recognizer = mock_recognizer_class.return_value
        mock_audio_file = mock_audio_file_class.return_value.__enter__.return_value
        mock_recognizer.record.return_value = 'audio_data'
        mock_recognizer.recognize_google.return_value = 'Hello World'

        transcription = speech2text.transcribe_audio('test_audio.wav')

        mock_audio_file_class.assert_called_with('test_audio.wav')
        mock_recognizer.record.assert_called_with(mock_audio_file)
        mock_recognizer.recognize_google.assert_called_with('audio_data')
        self.assertEqual(transcription, 'Hello World')

    @patch('speech2text.sr.AudioFile')
    @patch('speech2text.sr.Recognizer')
    def test_transcribe_audio_unknown_value_error(self, mock_recognizer_class, mock_audio_file_class):
        # Mock recognizer to raise UnknownValueError
        mock_recognizer = mock_recognizer_class.return_value
        mock_recognizer.recognize_google.side_effect = sr.UnknownValueError()

        transcription = speech2text.transcribe_audio('test_audio.wav')

        self.assertEqual(transcription, "Could not understand the audio.")

    @patch('speech2text.sr.AudioFile')
    @patch('speech2text.sr.Recognizer')
    def test_transcribe_audio_request_error(self, mock_recognizer_class, mock_audio_file_class):
        # Mock recognizer to raise RequestError
        mock_recognizer = mock_recognizer_class.return_value
        mock_recognizer.recognize_google.side_effect = sr.RequestError("API unavailable")

        transcription = speech2text.transcribe_audio('test_audio.wav')

        self.assertIn("Could not request results; API unavailable", transcription)

    @patch('speech2text.requests.get')
    def test_send_transcription_to_api_success(self, mock_get):
        # Simulate a successful API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Capture print output
        with patch('builtins.print') as mock_print:
            speech2text.send_transcription_to_api("Hello World")
            mock_print.assert_called_once_with("Transcription sent successfully!")

    @patch('speech2text.requests.get')
    def test_send_transcription_to_api_failure(self, mock_get):
        # Simulate a failed API response
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        # Capture print output
        with patch('builtins.print') as mock_print:
            speech2text.send_transcription_to_api("Hello World")
            mock_print.assert_called_once_with("Failed to send transcription. Status code: 500")

if __name__ == '__main__':
    unittest.main()
