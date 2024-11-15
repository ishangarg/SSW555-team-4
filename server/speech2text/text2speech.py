import sys
from gtts import gTTS

def text_to_speech(text, filename='output.mp3', lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        print(f"Audio content written to file '{filename}'")
    except Exception as e:
        print(f"An error occurred during text-to-speech conversion: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_text_file> [output_filename]")
        sys.exit(1)

    text_file_path = sys.argv[1]
    output_filename = sys.argv[2] if len(sys.argv) > 2 else 'output.mp3'

    try:
        with open(text_file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
    except FileNotFoundError:
        print(f"File not found: {text_file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

    if text_content:
        text_to_speech(text_content, output_filename)

if __name__ == '__main__':
    main()
