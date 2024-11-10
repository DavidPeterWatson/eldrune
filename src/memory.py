from mongodb import MongoDBHandler

class Memory():
    def __init__(self):
        self.campaigns = MongoDBHandler(
            database_name="eldrune_test",
            collection_name="campaigns"
        )

        self.players = MongoDBHandler(
            database_name="eldrune_test",
            collection_name="players"
        )

    def remember_campaign(self, campaign):
        campaign_id = self.campaigns.insert_one(campaign)
    
    def recall_campaigns(self):
        return self.campaigns.find_many()

    def remember_players(self, players):
        campaign_id = self.campaigns.insert_many(players)
    
    def recall_players(self, campaign):
        query = { "campaign": campaign['name'] }
        return self.campaigns.find_many(query)

def create_memory() -> Memory:
  
    return Memory()
