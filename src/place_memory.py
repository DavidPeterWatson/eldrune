from src.mongodb import MongoCollection
from pymongo import MongoClient
from pymongo.database import Database

class PlaceMemory():
    def __init__(self, db: Database):

        self.db = db
        self.places = MongoCollection(db, "places")
        self.places.collection.create_index( { 'lineage': 1 } )


    def remember_place(self, place):
        if self.recall_place(place['name']):
            raise Exception('a place with that name already exists')
        place['lineage'] = self.get_lineage(place)
        self.places.insert_one(place)
        return place


    def get_lineage(self, place):
        if 'encompassing_place' in place:
            encompassing_place_name = place['encompassing_place']
            encompassing_place = self.recall_place(encompassing_place_name)
            return f'{encompassing_place['lineage']},{place['name']}'
        else:
            return place['name']



    def recall_place(self, name):
        query = {'name': name}
        return self.places.find_one(query)


    def recall_places(self):
        return self.places.find_many()


    def forget_place(self, place):
        query = {'name': place['name']}
        return self.places.delete_one(query)


    def forget_all_places(self):
        return self.places.delete_many({})