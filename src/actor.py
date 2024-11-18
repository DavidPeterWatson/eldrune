from typing import Optional
from voice import OpenAiVoice
from listener import OpenAiListener

class Actor:
    def __init__(self):
        self.voice = OpenAiVoice()
        self.listener = OpenAiListener()

    def say(self, text: str) -> None:
        self.voice.say(text)

    def listen(self) -> Optional[str]:
        return self.listener.listen()

