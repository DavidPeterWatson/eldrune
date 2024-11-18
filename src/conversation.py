from typing import override
from openai import OpenAI
from openai import AssistantEventHandler
from actor import Actor
from assistant_context import AssistantContext
from tool import Tool

class Conversation(AssistantEventHandler):
    def __init__(self, assistant_id, assistant_context: AssistantContext, actor: Actor, client: OpenAI, completed_tool_name, completed_handler):
        super().__init__()
        self.status = 'busy'
        self.assistant_id = assistant_id
        self.assistant_context = assistant_context
        self.client = client
        self.messages = []
        self.thread = self.client.beta.threads.create()
        self.actor = actor
        self.completed_tool_name = completed_tool_name
        self.completed_handler = completed_handler
        self.status = 'busy'


    @override
    def on_event(self, event):
        print(event.event)
        if event.event == 'thread.run.requires_action':
            run_id = event.data.id
            self.handle_requires_action(event.data, run_id)
        if event.event == 'thread.message.completed':
            message = event.data.id
            self.handle_response(event.data, message)


    def find_tool(self, name) -> Tool:
        for tool in self.assistant_context.get_tools():
            if tool.get_definition()['function']['name'] == name:
                return tool


    def handle_requires_action(self, data, run_id):
      tool_outputs = []
        
      for tool_call in data.required_action.submit_tool_outputs.tool_calls:
          tool = self.find_tool(tool_call.function.name)
          output = tool.use(tool_call.function.arguments)
          tool_outputs.append({"tool_call_id": tool.id, "output": output})
          if tool_call.function.name == self.completed_tool_name:
              self.status = 'completed'

      self.submit_tool_outputs(tool_outputs, run_id)


    def submit_tool_outputs(self, tool_outputs, run_id):
        with self.client.beta.threads.runs.submit_tool_outputs_stream(
            thread_id=self.thread.id,
            run_id=run_id,
            tool_outputs=tool_outputs,
            event_handler=self,
        ) as stream:
            for text in stream.text_deltas:
                print(text, end="", flush=True)


# {
#   "id": "msg_abc123",
#   "object": "thread.message",
#   "created_at": 1698983503,
#   "thread_id": "thread_abc123",
#   "role": "assistant",
#   "content": [
#     {
#       "type": "text",
#       "text": {
#         "value": "Hi! How can I help you today?",
#         "annotations": []
#       }
#     }
#   ],
#   "assistant_id": "asst_abc123",
#   "run_id": "run_abc123",
#   "attachments": [],
#   "metadata": {}
# }



    def send_message(self, role: str, input: str) -> str:
        try:
            message = self.client.beta.threads.messages.create(
                thread_id=self.thread.id,
                role=role,
                content=input,
            )
            print(f'message: {message}', end="", flush=True)

            with self.client.beta.threads.runs.stream(
                thread_id=self.thread.id,
                assistant_id=self.assistant_id,
                # instructions=instructions,
                event_handler=self,
            ) as stream:
                stream.until_done()

        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"


    def run_conversation(self, instructions: str):
        self.send_message("user", instructions)

 

    def handle_response(self, message):
        text = message.content[0].text.value
        self.actor.say(text)
        if self.status == 'completed':
            self.completed_handler()
        player_input = self.actor.listen()
        self.send_message("user", player_input)
    