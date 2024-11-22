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


class GetCampaign(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self) -> object:
        return {
            'type': 'function',
            'function': {
                'name': 'get_saved_campaign',
                'description': 'Get the details of a remembered campaign',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'id': {
                            'type': 'string',
                            'description': 'Id of the remembered campaign',
                        },
                    },
                    'additionalProperties': False,
                },
            }
        }

    def use(self, arguments):
        campaign = json.loads(arguments)
        remembered_campaign = self.memory.recall_campaign(campaign['id'])
        return json.dumps(remembered_campaign)


class GetCurrentCampaign(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self) -> object:
        return {
            'type': 'function',
            'function': {
                'name': 'get_current_campaigns',
                'description': 'Get the details of the current campaign'
            }
        }

    def use(self, arguments):
        id = self.memory.current_campaign['id']
        return json.dumps(self.memory.recall_campaign(id))


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
        recalled_campaign = self.memory.recall_campaign_by_name(campaign['name'])
        if recalled_campaign:
            return 'Campaign with that name already exists. Please choose a different name'
        else:
            return json.dumps(self.memory.remember_campaign(campaign))


class ChangeCampaign(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self) -> object:
        return {
            'type': 'function',
            'function': {
                'name': 'change_campaign',
                'description': 'Remember changes to a campaign',
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
                        },
                        'theme': {
                            'type': 'string',
                            'description': 'Theme of the campaign.'
                        }
                    },
                    'required': ['id', 'name', 'setting', 'theme'],
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
