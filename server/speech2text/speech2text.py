# speech2text.py

import sys
import speech_recognition as sr
from pydub import AudioSegment
import os
import requests

def audio_file_to_wav(input_file):
    file_ext = os.path.splitext(input_file)[1].lower()
    if file_ext != '.wav':
        sound = AudioSegment.from_file(input_file)
        output_file = os.path.splitext(input_file)[0] + '.wav'
        sound.export(output_file, format='wav')
        return output_file
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

def send_transcription_to_api(transcription):
    url = "http://localhost:5000/data"
    params = {"transcription": transcription}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Transcription sent successfully!")
    else:
        print(f"Failed to send transcription. Status code: {response.status_code}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python speech2text.py <audio_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    wav_file = audio_file_to_wav(input_file)
    transcription = transcribe_audio(wav_file)
    print("Transcription:")
    print(transcription)
    # Uncomment the line below to send the transcription to the API, commented out as it does not currently have a database connection and will fail. 
    # send_transcription_to_api(transcription) 

if __name__ == '__main__':
    main()
