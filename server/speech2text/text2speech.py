import sys
from gtts import gTTS
import os

def text_to_speech(text, filename='output.mp3', lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        print(f"Audio content written to file '{filename}'")
    except Exception as e:
        print(f"An error occurred during text-to-speech conversion: {e}")

def main():
    # If no arguments provided, print usage and exit
    if len(sys.argv) < 2:
        print("Usage: python text2speech.py <path_to_text_file> [output_filename]")
        sys.exit(1)  # Exit the script if not enough arguments

    text_file_path = sys.argv[1]
    output_filename = sys.argv[2] if len(sys.argv) > 2 else 'output.mp3'
    text_content = None  # Initialize to None to avoid UnboundLocalError

    try:
        with open(text_file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
    except FileNotFoundError:
        print(f"File not found: {text_file_path}")
        sys.exit(1)  # Exit the script on file not found
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)  # Exit the script on any other file read errors

    # If text_content is empty or None, log an error and exit
    if not text_content:
        print("The file is empty or could not be read.")
        sys.exit(1)

    # If we have text content, proceed with text-to-speech conversion
    text_to_speech(text_content, output_filename)


if __name__ == '__main__':
    main()
