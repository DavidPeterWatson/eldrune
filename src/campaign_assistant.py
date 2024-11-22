from typing import List
from assistant_context import AssistantContext
from campaign_tools import GetCampaigns, SaveNewCampaign, ChooseCampaign
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
            return 'You are a friendly dungeon master for a table top role playing game called dungeons and dragons. The game is about to start but you need to find out which campaign the players want to play. The goal of this interaction is to find out which campaign, from the list of previously saved campaigns, the players want to play for this next session. Do not invent campaigns. Introduce yourself and welcome the players then share the names of the saved campaigns without any details, ask the players to choose a campaign, and then wait for the players input before continuing. If the players want to start a new campaign, then ask the players for a setting, theme and campaign name. Use the save_new_campaign function once the players have finished creating a new campaign. You can converse with players naturally and only when the players have chosen a campaign please call the choose_campaign function.'

    def get_tools(self) -> List[Tool]:
        return [
            self.get_campaigns,
            self.save_new_Campaign,
            self.choose_campaign,
            self.get_dungeon_master_name
        ]

    def get_completed_tool(self) -> Tool:
        return self.choose_campaign

