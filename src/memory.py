from pymongo import MongoClient
from src.event_memory import EventMemory
from src.mongodb import MongoCollection
from src.place_memory import PlaceMemory


class Memory():
    def __init__(self, database_name: str, host: str = 'localhost', port: int = 27017):
        self.host = host
        self.port = port 
        self.database_name = database_name

        self.place_memory = None
        self.event_memory = None

    def remember_campaign(self, campaign):
        id = ''
        if 'id' in campaign:
            query = {'id': campaign['id']}
            id = self.campaigns.update_one(query, campaign)
        else:
            id = self.campaigns.insert_one(campaign)
        return self.recall_campaign(id)


    def recall_campaign(self, id):
        query = {'id': id}
        return self.campaigns.find_one(query)


    def recall_campaign_by_name(self, name):
        query = {'name': name}
        return self.campaigns.find_one(query)


    def recall_campaigns(self):
        return self.campaigns.find_many()


    def forget_campaign(self, campaign):
        query = {'id': campaign['id']}
        return self.campaigns.delete_one(query)

    
    def remember_player(self, player):
        id = ''
        if 'id' in player:
            query = {'id': player['id']}
            id = self.players.update_one(query, player)
        else:
            id = self.players.insert_one(player)
        return self.recall_player(id)


    def remember_players(self, players):
        for player in players:
            self.remember_player(player)


    def recall_player(self, id):
        query = {'id': id}
        return self.players.find_one(query)


    def recall_players(self, campaign):
        query = {'campaign_id': campaign['id']}
        return self.players.find_many(query)


    def remember_thing(self, thing):
        id = ''
        if 'id' in thing:
            query = {'id': thing['id']}
            id = self.things.update_one(query, thing)
        else:
            id = self.things.insert_one(thing)
        return self.recall_thing(id)


    def recall_thing(self, id):
        query = {'id': id}
        return self.things.find_one(query)


    def recall_things(self, context):
        query = {'context': context}
        return self.things.find_many(query)


    def forget_thing(self, thing):
        query = {'id': thing['id']}
        return self.things.delete_one(query)
    

    def remember_setting(self, setting):
        id = ''
        if 'id' in setting:
            query = {'id': setting['id']}
            id = self.settings.update_one(query, setting)
        else:
            id = self.settings.insert_one(setting)
        return self.recall_setting(id)


    def recall_setting(self, id):
        query = {'id': id}
        return self.settings.find_one(query)


    def recall_setting(self):
        return self.settings.find_many()

    def __enter__(self):
        self.client = MongoClient(self.host, self.port)
        self.db = self.client[self.database_name]
        self.campaigns = MongoCollection(self.db, "campaigns")

        self.settings = MongoCollection(self.db, "settings")

        self.players = MongoCollection(self.db, "players")

        self.objects = MongoCollection(self.db, "objects")

        self.place_memory = PlaceMemory(self.db)
        self.event_memory = EventMemory(self.db)

        self.current_campaign = None
        self.current_setting = None
        return self

    def __exit__(self, *args):
        self.client.close()