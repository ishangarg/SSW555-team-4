class VoiceAssistant:
    def __init__(self, valid_commands):
        self.valid_commands = valid_commands

    def process_command(self, command):
        
        if not command:
            return "Error: I couldn't understand what you said. Can you please clarify?"

       
        if command not in self.valid_commands:
            return "Error: Something went wrong while generating a response. Try asking something else."

        
        return f"Processing command: {command}"

    def handle_system_error(self):
       
        return "Error: There was an issue. Please expect a delayed response or try again later."
