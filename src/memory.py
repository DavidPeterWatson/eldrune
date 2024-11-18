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
        self.current_campaign = None

    def remember_campaign(self, campaign):
        query = {'campaign_name': campaign['campaign_name'] }
        campaign_id = self.campaigns.find_one(query)
        if campaign_id:
            print(f'found campaign {campaign_id}')
        else:
            campaign_id = self.campaigns.insert_one(campaign)
    
    def recall_campaigns(self):
        return self.campaigns.find_many()

    def remember_player(self, player):
        query = {'player_name': player['player_name'] }
        player_id = self.players.find_one(query)
        if player_id:
            print(f'found player {player_id}')
        else:
            player_id = self.players.insert_one(player)

    def remember_players(self, players):
        for player in players:
            self.remember_player(player)
    
    def recall_players(self, campaign):
        return self.players.find_many()

def create_memory() -> Memory:
  
    return Memory()
