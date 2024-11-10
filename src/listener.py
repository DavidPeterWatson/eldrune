import speech_recognition as sr
from typing import Optional
from abc import ABC, abstractmethod
from openai import OpenAI

# AI Provider classes remain the same as before
class Listener(ABC):
    @abstractmethod
    def listen(self, timeout: int = 5) -> Optional[str]:
        pass


class OpenAiListener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
        self.recognizer.pause_threshold = 1.2

    def listen(self, timeout: int = 15) -> Optional[str]:
        try:
            print("\nListening...")
            with sr.Microphone() as source:
                audio = self.recognizer.listen(source, timeout=timeout)
            
                print("Processing speech...")
                text = self.recognizer.recognize_whisper_api(audio)
                print(f"You: {text}")
                return text
                
        except sr.WaitTimeoutError:
            print("No speech detected within timeout period")
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results: {str(e)}")
        except Exception as e:
            print(f"Error in speech recognition: {str(e)}")
        return None




class GoogleListener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.source = sr.Microphone()
        self.recognizer.pause_threshold = 1
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)

    def listen(self, timeout: int = 15) -> Optional[str]:
        try:
            print("\nListening...")
            with sr.Microphone() as source:
                audio = self.recognizer.listen(source, timeout=timeout)
                
                print("Processing speech...")
                text = self.recognizer.recognize_google(audio)
                print(f"You: {text}")
                return text
                
        except sr.WaitTimeoutError:
            print("No speech detected within timeout period")
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results: {str(e)}")
        except Exception as e:
            print(f"Error in speech recognition: {str(e)}")
        return None

        
def create_listener(provider_type: str) -> Listener: 
    if provider_type.lower() == 'python':
        return GoogleListener()

    elif provider_type.lower() == 'openai':
        return OpenAiListener()
    
    else:
        raise ValueError(f"Unknown provider type: {provider_type}")