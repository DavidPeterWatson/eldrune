from typing import List
from actor import Actor, create_actor
from memory import Memory, create_memory
from prompter import Prompter
from tools import join_property
from ai_provider import AI_PROVIDER_TYPE
import json
class GameMaster:
    def __init__(self, actor: Actor, memory: Memory, prompter: Prompter):
        self.actor = actor
        self.memory = memory
        self.prompter = prompter
        self.current_campaign = None
        self.current_players = None

    def run_choose_campaign_conversation(self):
        print(f"Starting conversation to choose campaign")
        campaigns = self.memory.recall_campaigns()
        if len(campaigns) == 0:
            choose_campaign_prompt = self.prompter.get_new_campaign_prompt(campaigns)
        else:
            choose_campaign_prompt = self.prompter.get_choose_campaign_prompt(campaigns)
        chosen_campaign = self.actor.run_conversation(choose_campaign_prompt, "campaign-name")
        print(f"chosen campaign: {chosen_campaign}")
        self.current_campaign = chosen_campaign
        self.memory.remember_campaign(self.current_campaign)

    def run_identify_players_conversation(self):
        print(f"Starting conversation to identify players")
        players = self.memory.recall_players(self.current_campaign)
        identify_players_prompt = self.prompter.get_players_prompt(players)
        self.current_players = self.actor.run_conversation(identify_players_prompt, "identified-players")
        self.memory.remember_players(self.current_players)

    def run_game(self):
        self.run_choose_campaign_conversation()
        self.run_identify_players_conversation()


def create_game_master(actor: Actor, memory: Memory, prompter: Prompter) -> GameMaster:
  
    return GameMaster(actor, memory, prompter)

def main():

    ai_provider_type = AI_PROVIDER_TYPE.OPEN_AI
    voice_provider_type = "openai"
    print(f"Initializing Game Master")
    try:
        actor = create_actor(ai_provider_type, voice_provider_type)
        memory = create_memory()
        prompter = Prompter()
        game_master = create_game_master(actor, memory, prompter)
        game_master.run_game()
    except KeyboardInterrupt:
        print("\nEnding conversation...")
    except Exception as e:
        print(f"Error initializing assistant: {str(e)}")

if __name__ == "__main__":
    main()