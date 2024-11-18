from assistant_context import AssistantContext
from tool import Tool
from memory import Memory


class GetPlayers(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self):
        return {
                'name': 'get_saved_campaigns',
                'description': 'Get a list of saved campaigns'
            }

    def use(self, arguments):
        return self.memory.recall_campaigns()
    

class SaveNewPlayer(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self):
        return   {
                'name': 'save_new_campaign',
                'description': 'Save a new campaign',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'name': {
                            'type': 'string',
                            'description': 'Name of the campaign.'
                        },
                        'setting': {
                            'type': 'string',
                            'description': 'Setting of the campaign.'
                        }
                    }
                }
            }

    def use(self, arguments):
        return self.memory.remember_campaign(arguments)


class ChoosePlayers(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_name(self):
        return 'Players Assistant'

    def get_definition():
        return {
                "name": "choose_campaign",
                "description": "Choose a campaign for this session",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Name of the campaign."
                        }
                    }
                }
            }

    def use(self, arguments):
        self.memory.current_campaign = arguments[0].name

class PlayerAssistantContext(AssistantContext):
    def __init__(self, memory: Memory):
        self.memory = memory
        self.get_players = GetPlayers(self.memory)
        self.save_new_player = SaveNewPlayer(self.memory)
        self.choose_players = ChoosePlayers(self.memory)

    def get_instructions(self):
            return 'You are the dungeon master for a table top role playing game called dungeons and dragons. Ask the players to identify themselves from the list or create a new player. If the player is new then ask them for the name of their character. After you have identified the players and all the required information respond only with a json formatted string using the following example ```json {"identified-players": [{"player_name": "player1_name", "character": { "name": "example_character_name", "class": "example_class", "ancestry": "example_ancestry"}}, {"player_name": "player2_name": "character": { "name": "example_character_name", "class": "example_class", "ancestry": "example_ancestry"}}]} ```'

    def get_tools(self):
        return [
            self.get_players,
            self.save_new_player,
            self.choose_players
        ]

    def get_completed_tool(self):
        return self.choose_players