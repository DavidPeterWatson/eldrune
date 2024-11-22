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

    def run_start_session(self):
        print(f"Starting conversation to identify players")
    #     players = self.memory.recall_players(self.current_campaign)
    #     identify_players_prompt = self.prompter.get_players_prompt(players)
    #     self.current_players = self.actor.run_conversation(identify_players_prompt, "identified-players")["identified-players"]
    #     print(f"current_players: {self.current_players}")
    #     self.memory.remember_players(self.current_players)

    def run_opening_scene(self):
        print(f"Starting conversation for opening scene of campaign")
        

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


