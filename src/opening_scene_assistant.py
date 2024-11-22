from typing import List
from assistant_context import AssistantContext
from campaign_tools import GetCampaign
from setting_tools import GetCurrentSetting
from dungeon_master_tools import GetDungeonMasterName
from tool import Tool
from memory import Memory
import json

class CampaignAssistantContext(AssistantContext):
    def __init__(self, memory: Memory):
        self.memory = memory
        self.get_dungeon_master_name = GetDungeonMasterName(self.memory)
        self.get_setting = GetCurrentSetting(self.memory)
        self.get_current_campaign = GetCampaign(self.memory)
        self.remember_context = RememberContext(self.memory)

    def get_name(self) -> str:
        return 'Campaign Assistant'

    def get_instructions(self) -> str:
            return 'You are a friendly dungeon master for a table top role playing game called dungeons and dragons. You are running a new campaign and are about to set the opening scene. First decide on a starting context that works for the current campaign theme and setting and remember it.'

    def get_tools(self) -> List[Tool]:
        return [
            self.get_current_campaign,
            self.get_setting,
            self.get_dungeon_master_name
        ]

    def get_completed_tool(self) -> Tool:
        return self.choose_campaign
