# Eldrune #

Eldrune is an AI driven table top role playing game master. The outcomes I seek are to play a ttrpg that is non-deterministic. Most ttrpg's are driven by campaigns where future events are predetermined to some extent. It takes humans a lot of effort to create worlds and stories that have continuity. Some people are great at creating rich engaging stories spontaneously with deep connections to past events and non-player characters with their own arcs. But I am not. So, maybe I can leverage AI to do it for me. I want to reveal the story as it goes, only unravelling world elements and story elements as the story progresses. This means only generating these just in time.

I will need co-ordinate a few different agents to achieve the desired results.

The architecture is as follows

User Interface
Text and voice
connects players to the Game Master
Displays response from game master

The game master service
Service accepting voice and text input from the ui
Sends requests to services for various operations and co-ordinates responses.

## Flow ##
Generate welcome narrative and ask who is playing.

### Pre Session ###
Identify players one at a time using voice recognition.
If not recognised then generate narrative asking for players name and what they want to get out of the game.
Send player response to role to convert to standard format json object.
Send json object to historian to remember.
Keep asking who is playing until no one responds or someone says that no-one else.

### Recap from Previous Session ###

### Opening Scene ###
Each scene has the following steps.
Historian will generate current context based on history. If no history then invent a interesting opening.
Generate context narrative from the current context including a question to players. What do they want to do? or why they are there? or what do they notice?
Host will share the narrative and ask players what they want to do.
Player response must woven back into history. As the history is added to the story arc, and npc arcs must be adjusted.
Details that players notice will be used to generate backstories and histories.
Actions that players want to take might require dice rolling or clarification.
Writer will generate changes to the environment based on the players actions.
Describe changes to the scene as a result of the players actions.

Adversary Agent is given a chance to react when a player rolls with fear or after a players action to spend fear tokens.

Keep asking players and adversaries what they want to do, resolving their actions and describing how the world responds until the scene ends.

The scene ending needs to align with beats in the story arc.

Story arcs will be used by the writer to influence how npc's actions and reactions.

### Session Closing ###

