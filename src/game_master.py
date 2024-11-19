from typing import List
from actor import Actor
from assistant import Assistant
from memory import Memory, create_memory
from campaign_assistant import CampaignAssistantContext
import secrets
class GameMaster:
    def __init__(self, memory: Memory, actor: Actor):
        self.memory = memory
        self.current_campaign = None
        self.current_players = None
        self.actor = actor


    # def run_choose_campaign_conversation(self):
    #     print(f"Starting conversation to choose campaign")
    #     campaigns = self.memory.recall_campaigns()
    #     if len(campaigns) == 0:
    #         choose_campaign_prompt = self.prompter.get_new_campaign_prompt(campaigns)
    #     else:
    #         choose_campaign_prompt = self.prompter.get_choose_campaign_prompt(campaigns)

    #     chosen_campaign = self.actor.run_conversation(choose_campaign_prompt, "campaign_name")
        
    #     print(f"chosen campaign: {chosen_campaign}")
    #     self.current_campaign = chosen_campaign
    #     self.memory.remember_campaign(self.current_campaign)

    def run_choose_campaign_conversation(self):
        print(f"Starting conversation to choose campaign")
        campaign_assistant_context = CampaignAssistantContext(self.memory)
        campaign_assistant = Assistant(campaign_assistant_context)
        campaign_assistant.run_conversation(self.actor)


    def run_identify_players_conversation(self):
        print(f"Starting conversation to identify players")
    #     players = self.memory.recall_players(self.current_campaign)
    #     identify_players_prompt = self.prompter.get_players_prompt(players)
    #     self.current_players = self.actor.run_conversation(identify_players_prompt, "identified-players")["identified-players"]
    #     print(f"current_players: {self.current_players}")
    #     self.memory.remember_players(self.current_players)

    # def run_start_campaign(self):
    #     print(f"Starting conversation to identify players")
    #     players = self.memory.recall_players(self.current_campaign)
    #     identify_players_prompt = self.prompter.get_players_prompt(players)
    #     self.current_players = self.actor.run_conversation(identify_players_prompt, "identified-players")["identified-players"]
    #     print(f"current_players: {self.current_players}")
    #     self.memory.remember_players(self.current_players)

    def run_game(self):
        self.run_choose_campaign_conversation()
        self.run_identify_players_conversation()


def main():

    print(f"Initializing Game Master")
    try:
        memory = create_memory()
        actor = Actor()
        game_master = GameMaster(memory, actor)
        game_master.run_game()
    except KeyboardInterrupt:
        print("\nEnding conversation...")
    except Exception as e:
        print(f"Error initializing assistant: {str(e)}")

if __name__ == "__main__":
    main()


