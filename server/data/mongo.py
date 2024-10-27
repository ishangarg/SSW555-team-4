from pymongo import MongoClient


class Mongo:

    def __init__(self) -> None:
        self.client = MongoClient("mongodb://localhost:27017/")

    def new_conversation(self, data):
        pass
    
    def add_conversation(self, data):
        pass
    
    def remove_conversation(self, data):
        pass

    def new_mood(self, data):
        pass

    def update_mood(self, data):
        pass

    def remove_mode(self, data):
        pass