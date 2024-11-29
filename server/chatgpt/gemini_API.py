import vertexai
from vertexai.generative_models import GenerativeModel, Part
import requests
import google.cloud.storage as gcs
# TODO(developer): Update and un-comment below line
# PROJECT_ID = "your-project-id"
import json

# FILENAME = "/Users/ishangarg/Downloads/SSS555/server/speech2text/your_audio_file.mp3"

def json_parser(gpt_output):
    if gpt_output.startswith("```json"):
        gpt_output = gpt_output[7:]
    if gpt_output.endswith(""):
        gpt_output = gpt_output[:-4]

    print(gpt_output)
    try:
        parsed_output = json.loads(gpt_output)
    except json.JSONDecodeError as e:
        # logging.error(f"JSONDecodeError: {e}")
        parsed_output = {}

    return parsed_output

def transcribe_and_get_mood(filename):

    vertexai.init(project='ramp-sheet', location="us-central1")

    model = GenerativeModel("gemini-1.5-flash-002")

    prompt = """
    Objective:
    Provide a transcription and sentiment analysis of an audio file based on its transcription and modulation patterns.

    Step 1: Transcription Summary
    Task:
    Transcribe the content of the audio file into text.

    Focus on clarity and accuracy, ensuring all speech is transcribed.
    Capture any key phrases, important terms, or emotional cues.
    Deliverable:
    The exact transcript of the audio file.

    Step 2: Sentiment Analysis
    Task:
    Perform sentiment analysis on the transcription text, identifying the general emotional tone of the content. Analyze for sentiment categories such as:

    Positive
    Negative
    Neutral
    Mixed
    Deliverable:
    Provide a score of the sentiment analysis. 0 being a negative emotion and 10 being a positive emotion.

    Step 3: Audio Modulation Analysis
    Task:
    Analyze the audio modulation (tone, pitch, speed, pauses) for emotional cues beyond the words themselves. Focus on:

    Tone: Is it calm, agitated, happy, sad, etc.?
    Pitch: High-pitched (excitement, nervousness) or low-pitched (anger, calm)?
    Speed: Is the speaker speaking quickly (eagerness, urgency) or slowly (calm, hesitant)?
    Pauses: Are there significant pauses or changes in rhythm? What might these signify (contemplation, uncertainty, emphasis)?
    Deliverable:
    Provide a detailed interpretation of the audio's emotional tone based on these factors. Explain how the speaker's vocal characteristics support or contrast the textual sentiment analysis.

    Final Report:
    Provide a transcrption of the audio:
    Provide a sentiment score  on a scale of 0-10(0 being the negative emotion and 10 being highly positive emotion).
    Give me the entire result as a json with two fields - trancript, sentiment_score, emotion which is a text which contains field Happy, Neutral, Sad, Angry. That's it.
    """

    # Upload to Google Cloud Storage
    storage_client = gcs.Client()
    bucket = storage_client.bucket("voiceanalysis")
    blob = bucket.blob("your_audio_file.mp3")
    blob.upload_from_filename(filename)

    # Get the public URL
    public_url = blob.public_url

    # Create the request
    audio_file_uri = public_url
    print(public_url)

    audio_file = Part.from_uri(audio_file_uri, mime_type="audio/mp3")

    contents = [audio_file, prompt]

    response = model.generate_content(contents)
    print(response.text)
    return json_parser(response.text)
    # Example response:
    # **Made By Google Podcast Summary**
    # **Chapter Titles:**
    # * Introduction
    # * Transformative Pixel Features
    # ...

# transcribe_and_get_mood(FILENAME)