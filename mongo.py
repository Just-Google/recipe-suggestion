from pymongo import MongoClient
import api

class Database:
    client = MongoClient('localhost', 27017)
    db = client["ubhacking"]
    collection = db["recipe-collection"]

    def __init__(self):
        if self.collection.find_one({}) == None:
            api.get_recipe_multithread(self)
        return

    def get(self, item):
        recipes = self.collection.find(item)    
        
        return list(recipes)

    def insert(self, item):
        if self.collection.find_one(item) == None:
            self.collection.insert_one(item)
