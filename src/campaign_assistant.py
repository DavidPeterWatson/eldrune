from typing import List
from assistant_context import AssistantContext
from tool import Tool
from memory import Memory
import json

class GetCampaigns(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self) -> object:
        return {
            'type': 'function',
            'function': {
                'name': 'get_saved_campaigns',
                'description': 'Get a list of saved campaigns',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'test': {
                            'type': 'string',
                            'description': 'Nothing',
                        },
                    },
                    'additionalProperties': False,
                },
            }
        }

    def use(self, arguments):
        return json.dumps(self.memory.recall_campaigns())
    

class SaveNewCampaign(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self) -> object:
        return {
            'type': 'function',
            'function': {
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
                    },
                    'required': ['name', 'setting'],
                    'additionalProperties': False
                }
            }
        }
    
    def use(self, arguments):
        return json.dumps(self.memory.remember_campaign(arguments))


class ChooseCampaign(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self) -> object:
        return {
            'type': 'function',
            'function': {
                'name': 'choose_campaign',
                'description': 'Choose a campaign for this session',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'name': {
                            'type': 'string',
                            'description': 'Name of the campaign.'
                        }
                    },
                    'required': ['name'],
                    'additionalProperties': False
                }
            }
        }


    def use(self, arguments):
        print(str(arguments))
        chosen_campaign = json.loads(arguments)
        self.memory.current_campaign = chosen_campaign
        return ''

class CampaignAssistantContext(AssistantContext):
    def __init__(self, memory: Memory):
        self.memory = memory
        self.get_campaigns = GetCampaigns(self.memory)
        self.save_new_Campaign = SaveNewCampaign(self.memory)
        self.choose_campaign = ChooseCampaign(self.memory)

    def get_name(self) -> str:
        return 'Campaign Assistant'

    def get_instructions(self) -> str:
            return 'You are the dungeon master for a table top role playing game called dungeons and dragons. The game is about to start but you need to find out which campaign the players want to play. Do not make decisions for the players. The goal of this interaction is to find out which campaign, from the list of previously saved campaigns, the players want to play for this next session. Do not invent new campaigns. Share the names of the campaigns first without any detail and ask the players to choose a campaign, and then wait for the players input before continuing. You can converse with players naturally and only when the players have chosen a campaign please call the choose_campaign function.'

    def get_tools(self) -> List[Tool]:
        return [
            self.get_campaigns,
            self.save_new_Campaign,
            self.choose_campaign
        ]

    def get_completed_tool(self) -> Tool:
        return self.choose_campaign
