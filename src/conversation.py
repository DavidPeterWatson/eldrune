from ai_provider import AIProvider, create_ai_provider, AI_PROVIDER_TYPE


class Conversation:
    def __init__(self, ai_provider: AIProvider):
        self.ai_provider = ai_provider
        self.messages = []

    def get_ai_response(self, role: str, input: str) -> str:
        """Get response from current AI provider"""
        try:
            self.messages.append({"role": role, "content": input})
            response = self.ai_provider.get_response(self.messages)
            self.messages.append({"role": "assistant", "content": response})
            return response
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

        
def create_conversation(provider_type: AI_PROVIDER_TYPE = AI_PROVIDER_TYPE.OPEN_AI) -> Conversation:
    ai_provider = create_ai_provider(provider_type)
    return Conversation(ai_provider)