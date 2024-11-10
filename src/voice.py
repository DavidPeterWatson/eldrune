from typing import List
import pygame
import pyttsx3
import tempfile

import os
from abc import ABC, abstractmethod
from pathlib import Path
from openai import OpenAI

# AI Provider classes remain the same as before
class Voice(ABC):
    @abstractmethod
    def say(self, text: str) -> None:
        pass

class VoiceConfig:
    """Configuration class for WaveNet voices"""
    def __init__(
        self,
        language_code: str = "en-GB",
        name: str = "en-GB-Neural2-F",  # Female voice
        speaking_rate: float = 1.0,
        pitch: float = 0.0
    ):
        self.language_code = language_code
        self.name = name
        self.speaking_rate = speaking_rate
        self.pitch = pitch

class OpenAiVoice(Voice):
    def __init__(self):
        self.client = OpenAI()
        self.speech_file_path = Path(__file__).parent / "speech.mp3"
        pygame.mixer.init()

    def say(self, text: str) -> None:
        print(f"\nsaying: {text}")
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="fable",
            input=text
        )
        print(f"\nwaiting for speech")
        response.stream_to_file(self.speech_file_path)

        # Play the audio
        pygame.mixer.music.load(self.speech_file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # Clean up temporary file
        os.unlink(self.speech_file_path)

# class WaveNetVoice(Voice):
#     """Handles text-to-speech using Google Cloud WaveNet"""
#     def __init__(self, voice_config: VoiceConfig):
#         self.client = tts.TextToSpeechClient()
#         self.voice_config = voice_config
#         self.voice = tts.VoiceSelectionParams(
#             language_code=voice_config.language_code,
#             name=voice_config.name
#         )
#         self.audio_config = tts.AudioConfig(
#             audio_encoding=tts.AudioEncoding.MP3,
#             speaking_rate=voice_config.speaking_rate,
#             pitch=voice_config.pitch
#         )
#         pygame.mixer.init()

#     def say(self, text: str) -> None:
#         """Convert text to speech using WaveNet and play it"""
#         try:
#             # Split long text into smaller chunks (WaveNet has a character limit)
#             chunks = self._split_text(text)
            
#             for chunk in chunks:
#                 # Synthesize speech
#                 synthesis_input = tts.SynthesisInput(text=chunk)
#                 response = self.client.synthesize_speech(
#                     input=synthesis_input,
#                     voice=self.voice,
#                     audio_config=self.audio_config
#                 )

#                 # Save and play the audio
#                 with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
#                     temp_file.write(response.audio_content)
#                     temp_file_path = temp_file.name

#                 # Play the audio
#                 pygame.mixer.music.load(temp_file_path)
#                 pygame.mixer.music.play()
#                 while pygame.mixer.music.get_busy():
#                     pygame.time.Clock().tick(10)

#                 # Clean up temporary file
#                 os.unlink(temp_file_path)

#         except Exception as e:
#             print(f"Error in text-to-speech: {str(e)}")
            
#     def _split_text(self, text: str, max_chars: int = 1000) -> List[str]:
#         """Split text into smaller chunks for WaveNet processing"""
#         chunks = []
#         current_chunk = ""
        
#         sentences = text.split('. ')
#         for sentence in sentences:
#             if len(current_chunk) + len(sentence) < max_chars:
#                 current_chunk += sentence + '. '
#             else:
#                 chunks.append(current_chunk)
#                 current_chunk = sentence + '. '
        
#         if current_chunk:
#             chunks.append(current_chunk)
            
#         return chunks


class PythonVoice(Voice):
    def __init__(self,):
        self.engine = pyttsx3.init()
  
        # Configure text-to-speech
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        
    def say(self, text: str) -> None:
        """Convert text to speech and read it aloud"""
        print(f"\nAssistant: {text}")
        sentences = text.split('. ')
        for sentence in sentences:
            if sentence:
                self.engine.say(sentence)
                self.engine.runAndWait()


def create_voice(voice_provider_type):
    if voice_provider_type.lower() == 'python':
        return PythonVoice()
    
    # elif provider_type.lower() == 'google':
    #     if voice_config is None:
    #         voice_config = VoiceConfig()
    #     return WaveNetVoice(voice_config)
    
    elif voice_provider_type.lower() == 'openai':
        return OpenAiVoice()
    
    else:
        raise ValueError(f"Unknown voice provider type: {voice_provider_type}")