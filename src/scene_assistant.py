from typing import List
from assistant_context import AssistantContext
from tool import Tool
from memory import Memory
import json
class CampaignAssistantContext(AssistantContext):
    def __init__(self, memory: Memory):
        self.memory = memory
        self.get_campaigns = GetCampaigns(self.memory)
        self.save_new_Campaign = SaveNewCampaign(self.memory)
        self.choose_campaign = ChooseCampaign(self.memory)
        self.get_dungeon_master_name = GetDungeonMasterName(self.memory)

    def get_name(self) -> str:
        return 'Campaign Assistant'

    def get_instructions(self) -> str:
            return 'You are a friendly dungeon master for a table top role playing game called dungeons and dragons. Use the current scene context to describe to the players what their characters can see, and then ask the players what they want to do. If players want more detail then you can get scene details and describe what they see. Some details might require the players to roll to see how much detail they can perceive. If a roll is required then ask the player to roll the dice required by the scene details. Use the get scene details function again with the dice values, describe to the players what their character sees and wait for the players to make their next request. When the scene ends then use the scene_end tool. The scene ends when the story moves to a different place. Provide a summary of the current scene.'

    def get_tools(self) -> List[Tool]:
        return [
            self.get_current_scene_context,
            self.get_scene_details,
            self.save_scene,
            self.get_dungeon_master_name
        ]

    def get_completed_tool(self) -> Tool:
        return self.choose_campaign

class GetDungeonMasterName(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self) -> object:
        return {
            'type': 'function',
            'function': {
                'name': 'get_dungeon_master_name',
                'description': 'Get the name of the dungeon master'
                # 'parameters': {
                #     'type': 'object',
                #     # 'properties': {
                #     #     'name': {
                #     #         'type': 'string',
                #     #         'description': 'Nothing',
                #     #     },
                #     # },
                #     'additionalProperties': False,
                # },
            }
        }

    def use(self, arguments):
        return 'Jeeves'
    
class GetCampaigns(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self) -> object:
        return {
            'type': 'function',
            'function': {
                'name': 'get_saved_campaigns',
                'description': 'Get a list of saved campaigns',
                # 'parameters': {
                #     'type': 'object',
                #     'properties': {
                #         'test': {
                #             'type': 'string',
                #             'description': 'Nothing',
                #         },
                #     },
                #     'additionalProperties': False,
                # },
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
        campaign = json.loads(arguments)
        return json.dumps(self.memory.remember_campaign(campaign))


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
                        'id': {
                            'type': 'string',
                            'description': 'id of the campaign.'
                        },
                        'name': {
                            'type': 'string',
                            'description': 'Name of the campaign.'
                        }
                    },
                    'required': ['id', 'name'],
                    'additionalProperties': False
                }
            }
        }


    def use(self, arguments):
        print(str(arguments))
        chosen_campaign = json.loads(arguments)
        self.memory.current_campaign = chosen_campaign
        return ''

class ForgetCampaign(Tool):
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
                        'id': {
                            'type': 'string',
                            'description': 'id of the campaign.'
                        },
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
        campaign = json.loads(arguments)
        return json.dumps(self.memory.forget_campaign(campaign))
