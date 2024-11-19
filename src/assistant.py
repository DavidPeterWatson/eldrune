from assistant_context import AssistantContext
from conversation import Conversation
from openai import OpenAI
from openai_constants import OpenAIModel


class Assistant():
    def __init__(self, assistant_context: AssistantContext):
        self.client = OpenAI()
        self.assistant_context = assistant_context
        self.name = self.assistant_context.get_name()
        self.tools = list(map(lambda t: t.get_definition(), self.assistant_context.get_tools()))
        self.instructions = self.assistant_context.get_instructions()

        self.assistant = self.client.beta.assistants.create(
            name=self.name,
            instructions=self.instructions,
            tools=self.tools,
            model=OpenAIModel.GPT_4_MINI,
        )


    def run_conversation(self, actor):
        conversation = Conversation(self.assistant.id, self.assistant_context, actor, self.client)
        conversation.run_conversation(self.assistant_context.get_instructions())
