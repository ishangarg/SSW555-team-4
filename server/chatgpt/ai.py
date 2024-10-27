import openai

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