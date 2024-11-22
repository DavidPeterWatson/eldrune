from memory import Memory
from tool import Tool


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
   