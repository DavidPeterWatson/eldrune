from enum import StrEnum
from typing import Dict, List
import anthropic
import openai
import os
from abc import ABC, abstractmethod
import secrets

class AI_PROVIDER_TYPE(StrEnum):
    CLAUDE = 'claude'
    OPEN_AI = 'openai'

# AI Provider classes remain the same as before
class AIProvider(ABC):
    @abstractmethod
    def get_response(self, messages: List[Dict[str, str]]) -> str:
        pass

class ClaudeProvider(AIProvider):
    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        
    def get_response(self, messages: List[Dict[str, str]]) -> str:
        try:
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=128,
                messages=messages
            )
            return response.content[0].text
        except Exception as e:
            return f"Claude API error: {str(e)}"

class OpenAIModel(StrEnum):
    GPT_4_MINI = 'gpt-4o-mini'
    GPT_3_5_TURBO = 'gpt-3.5-turbo'

class OpenAIProvider(AIProvider):
    def __init__(self, api_key: str):
        self.client = openai.Client(api_key=api_key)
        
    def get_response(self, messages: List[Dict[str, str]]) -> str:
        try:
            print(messages)
            response = self.client.chat.completions.create(
                model=OpenAIModel.GPT_4_MINI,
                messages=messages,
                max_tokens=128
            )
            print(response)
            return response.choices[0].message.content
        except Exception as e:
            return f"OpenAI API error: {str(e)}"

def create_ai_provider(provider_type: AI_PROVIDER_TYPE):
    if provider_type == AI_PROVIDER_TYPE.CLAUDE:
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")
        return ClaudeProvider(api_key)

    elif provider_type == AI_PROVIDER_TYPE.OPEN_AI:
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        return OpenAIProvider(api_key)

    else:
        raise ValueError(f"Unknown provider type: {provider_type}")
