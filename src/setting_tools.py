from tool import Tool
from memory import Memory
import json

class GetSettings(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self) -> object:
        return {
            'type': 'function',
            'function': {
                'name': 'get_remembered_settings',
                'description': 'Get a list of remembered settings',
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
        return json.dumps(self.memory.recall_settings())
    

class RememberNewSetting(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self) -> object:
        return {
            'type': 'function',
            'function': {
                'name': 'remember_new_setting',
                'description': 'Remember a new setting',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'name': {
                            'type': 'string',
                            'description': 'Name of the setting.'
                        },
                        'setting': {
                            'type': 'string',
                            'description': 'Setting of the setting.'
                        }
                    },
                    'required': ['name', 'setting'],
                    'additionalProperties': False
                }
            }
        }
    
    def use(self, arguments):
        setting = json.loads(arguments)
        recalled_setting = self.memory.recall_setting_by_name(setting['name'])
        if recalled_setting:
            return 'Setting with that name already exists. Please choose a different name'
        else:
            remembered_setting = json.dumps(self.memory.remember_setting(setting))



class ChangeSetting(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self) -> object:
        return {
            'type': 'function',
            'function': {
                'name': 'change_setting',
                'description': 'Remember changes to a setting',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'id': {
                            'type': 'string',
                            'description': 'id of the setting.'
                        },
                        'name': {
                            'type': 'string',
                            'description': 'Name of the setting.'
                        },
                        'setting': {
                            'type': 'string',
                            'description': 'Setting of the setting.'
                        },
                        'theme': {
                            'type': 'string',
                            'description': 'Theme of the setting.'
                        }
                    },
                    'required': ['id', 'name', 'setting', 'theme'],
                    'additionalProperties': False
                }
            }
        }
    
    def use(self, arguments):
        setting = json.loads(arguments)
        return json.dumps(self.memory.remember_setting(setting))


class ChooseSetting(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self) -> object:
        return {
            'type': 'function',
            'function': {
                'name': 'choose_setting',
                'description': 'Choose a setting for this session',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'id': {
                            'type': 'string',
                            'description': 'id of the setting.'
                        },
                        'name': {
                            'type': 'string',
                            'description': 'Name of the setting.'
                        }
                    },
                    'required': ['id', 'name'],
                    'additionalProperties': False
                }
            }
        }


    def use(self, arguments):
        print(str(arguments))
        chosen_setting = json.loads(arguments)
        self.memory.current_setting = chosen_setting
        return ''

class GetCurrentSetting(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self) -> object:
        return {
            'type': 'function',
            'function': {
                'name': 'get_current_setting',
                'description': 'Get the current setting for this session'
            }
        }


    def use(self, arguments):
        print(str(arguments))
        return self.memory.current_setting

    
class ForgetSetting(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self) -> object:
        return {
            'type': 'function',
            'function': {
                'name': 'save_new_setting',
                'description': 'Save a new setting',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'id': {
                            'type': 'string',
                            'description': 'id of the setting.'
                        },
                        'name': {
                            'type': 'string',
                            'description': 'Name of the setting.'
                        },
                        'setting': {
                            'type': 'string',
                            'description': 'Setting of the setting.'
                        }
                    },
                    'required': ['name', 'setting'],
                    'additionalProperties': False
                }
            }
        }
    
    def use(self, arguments):
        setting = json.loads(arguments)
        return json.dumps(self.memory.forget_setting(setting))
