# speech2text.py

import speech_recognition as sr
from pydub import AudioSegment
import os

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

def main():
    input_file = 'your_audio_file.mp3'  # Replace with your file path
    wav_file = convert_audio_to_wav(input_file)
    transcription = transcribe_audio(wav_file)
    print("Transcription:")
    print(transcription)

if __name__ == '__main__':
    main()
