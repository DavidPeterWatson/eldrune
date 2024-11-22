from tool import Tool
from memory import Memory
import json

class GetContext(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self) -> object:
        return {
            'type': 'function',
            'function': {
                'name': 'get_context',
                'description': 'Describe the events that lead up to the given place and time',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'place': {
                            'type': 'string',
                            'description': 'The name of the place for the context',
                        },
                        'time': {
                            'type': 'string',
                            'description': 'The time for the context',
                        },
                    },
                    'additionalProperties': False,
                },
            }
        }

    def use(self, arguments):
        self.memory.recall_things
        
    
class RememberEvent(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self) -> object:
        return {
            'type': 'function',
            'function': {
                'name': 'create_',
                'description': 'Remember the context',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'place_id': {
                            'type': 'string',
                            'description': 'The place or location where an event occurred',
                        },
                        'Time': {
                            'type': 'string',
                            'description': 'The time that an event occurred',
                        },
                    },
                    'additionalProperties': True,
                },
            }
        }

    def use(self, arguments):
        event = json.loads(arguments)
        return json.dumps(self.memory.remember_event(event))



class ForgetEvent(Tool):
    def __init__(self, memory: Memory):
        self.memory = memory

    def get_definition(self) -> object:
        return {
            'type': 'function',
            'function': {
                'name': 'forget_event',
                'description': 'Forget an event happened. This removes the event from memory',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'id': {
                            'type': 'string',
                            'description': 'id of the campaign.'
                        }
                    },
                    'required': ['id'],
                    'additionalProperties': False
                }
            }
        }
    
    def use(self, arguments):
        campaign = json.loads(arguments)
        return json.dumps(self.memory.forget_event(campaign))
