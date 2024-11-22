from pymongo.database import Database
from src.mongodb import MongoCollection

class EventMemory():
    def __init__(self, db: Database):
        self.db = db
        self.events = MongoCollection(db, "events")


    def remember_event(self, event):
        id = ''
        if 'id' in event:
            query = {'id': event['id']}
            return self.events.update_one(query, event)
        else:
            return self.events.insert_one(event)


    def recall_event(self, id):
        query = {'id': id}
        return self.events.find_one(query)


    def get_context(self, place, time):
        place_id = place['id']
        time_id = time['id']
        query = { 'place': f'/^,{place_id},/', 'time': f'/^,{time_id},/' }
        return self.events.find_many(query)


    def forget_event(self, event):
        query = {'id': event['id']}
        return self.events.delete_one(query)


    def forget_all_events(self):
        return self.events.delete_many()
