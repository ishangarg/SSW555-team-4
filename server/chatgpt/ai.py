import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# Check if the API key is loaded properly
if not API_KEY:
    raise EnvironmentError("API key not found. Ensure 'OPENAI_API_KEY' is set in the .env file.")

def chatgpt(query):
    """
    Function to query ChatGPT using the provided API key and query string.
    """
    try:
        openai.api_key = API_KEY  # Set the API key

        # Send the query to ChatGPT
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query},
            ]
        )
        # Extract and return the assistant's response
        return response.choices[0].message.content#["content"]
    except Exception as e:
        return f"An error occurred: {e}"

class AI:
    """
    AI class to encapsulate the OpenAI API integration.
    """

    def __init__(self, key) -> None:
        if not key:
            raise ValueError("API key must be provided.")
        self.key = key
        openai.api_key = key  # Set the API key for this instance
    
    # def get_chatgpt_response(self, query):
    #     """
    #     Method to query ChatGPT and return its response.
    #     """
    #     try:
    #         response = openai.ChatCompletion.create(
    #             model="gpt-3.5-turbo",
    #             messages=[
    #                 {"role": "system", "content": "You are a helpful assistant."},
    #                 {"role": "user", "content": query},
    #             ]
    #         )
    #         return response['choices'][0]['message']['content']
    #     except Exception as e:
    #         return f"An error occurred: {e}"

if __name__ == '__main__':
    # Instantiate the AI class
    ai = AI(API_KEY)
    
    # Example query
    query = "What is the capital of France?"
    
    # Get response using the chatgpt function
    function_response = chatgpt(API_KEY, query)
    print("Response from chatgpt function:", function_response)
    
    # Get response using the AI class method
    # class_response = ai.get_chatgpt_response(query)
    # print("Response from AI class method:", class_response)
