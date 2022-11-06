from pymongo import MongoClient

class Database:
    client = MongoClient('localhost', 27017)
    db = client["ubhacking"]
    collection = db["recipe-collection"]

    def __init__(self):

        return

    def get(self, item):
        recipes = self.collection.find(item)    
        
        return list(recipes)

    def insert(self, item):
        if self.collection.find_one(item) == None:
            self.collection.insert_one(item)
