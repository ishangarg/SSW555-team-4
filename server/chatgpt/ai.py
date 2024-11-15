import openai

def chatgpt(api_key, query):
    try:
        # Set the OpenAI API key
        openai.api_key = api_key

        # Send the query to ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}]
        )

        # Retrieve and return the response content
        return response['choices'][0]['message']['content']
    except Exception as e:
        # Handle exceptions gracefully
        return f"An error occurred: {e}"
    
class AI:

    def __init__(self, key) -> None:
        self.key = key
        openai.api_key = key
    
    def get_chatgpt_response(self, query):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}]
        )
        return response['choices'][0]['message']['content']