from typing import Optional
from voice import create_voice
from listener import create_listener
from conversation import create_conversation
from ai_provider import AI_PROVIDER_TYPE
from tools import extract_json

class Actor:
    def __init__(self, ai_provider_type: AI_PROVIDER_TYPE, voice_provider_type):
        self.voice = create_voice(voice_provider_type)
        self.listener = create_listener(voice_provider_type)
        self.ai_provider_type = ai_provider_type

    def say(self, text: str) -> None:
        self.voice.say(text)

    def listen(self, timeout: int = 5) -> Optional[str]:
        return self.listener.listen()

    def run_conversation(self, prompt: str, conclusion_key: str):
        conversation = create_conversation(self.ai_provider_type)
        ai_response = conversation.get_ai_response("system", prompt)
        self.say(ai_response)

        while True:
            player_input = self.listen()
            
            if not player_input:
                self.say("I didn't catch that. Could you please repeat?")
                continue
                
            ai_response = conversation.get_ai_response("user", player_input)
            json_response = extract_json(ai_response)
            if json_response is not None:
                return json_response

            self.say(ai_response)

   
def create_actor(ai_provider_type: AI_PROVIDER_TYPE, voice_provider_type) -> Actor:
    return Actor(ai_provider_type, voice_provider_type)