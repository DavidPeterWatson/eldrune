# Eldrune Design #

## High Level Design ##

User Interface has the following elements
- Game Master interaction natural language processing with voice and text
- Narrative view. Scrollable view of narrative to see the latest and scroll back in history to see what happened.
- Map view
- Character View. The players character stats

Services layer
Contains user journey services
The Coordinator will co-ordinate the interactions between the various services.
The Game Master AI will be asked to interact with players to provide specific feedback.
The History Service will provide a recording of all events in the story world.
The Historian will provide a context for any given place and time using the history service.
The Narrator will provide a narrative based on the context for the game master to share with the players.
The World-Builder will insert events into the story worlds' history to explain the occurrence of any story element. Seeks continuity and wonder. Story arcs and character arcs.
The Map-Builder will create maps from story history.





## Flow ##
User Interface - Ask Game Master to Start Game
Game Master -> Ask narrator to welcome the players to identify themselves and their character. -> Dialog & Player data
if dialog 
Game Master -> Actor Speak dialog and interpret response
Game Master -> narrator response

if player data
Game Master -> Library Save Player data


Coordinator -> Ask world-builder to create opening scene context -> scene context
Coordinator -> Game Master. Provide context and ask game master to narrate and ask the characters what they want to do.
Game Master -> Coordinator Provide next narrative
Coordinator -> Script. check that narrative has continuity
Coordinator -> Game Master last story event is discontinuous. please amend.

Coordinator -> Game Master Continue


Send json object to historian to remember.
Keep asking who is playing until no one responds or someone says that no-one else.



Capabilities
Narrator Agent
    Generate narrative(opening and ask who is playing)


Host Service
    Ask for input (text Narrative) text response

Agent
    Convert text to player json

Historian
    Remember Player


The user interface will be mostly voice and text driven. Multiple players can interact with the game master any time they want to with text, but only when prompted by voice. Each player will have their own device for text based interaction.



Coordinator to Game Master
"
You are the game master for a table top role playing game called dungeons and dragons. Give yourself a friendly name and introduce yourself. Welcome the players to the game. Ask them to identify themselves one by one, and with follow up questions determine each players real name and the characters' name, ancestry and class they are playing. Check that the players have provided standard dungeons and dragons ancestry names and class names with follow up suggestions if their request was not correct. Once all payers have been identified, respond with a json formatted output in the following format {"player1_name": { "character": { "name": "example_character_name", "class": "example_class", "ancestry": "example_ancestry"}}, "player2_name": { "character": { "name": "example_character_name", "class": "example_class", "ancestry": "example_ancestry"}}}
"

{
  "David": { 
    "character": { 
      "name": "Puck", 
      "class": "wizard", 
      "ancestry": "elf" 
    }
  },
  "Arya": { 
    "character": { 
      "name": "Erdra Earthsong", 
      "class": "druid", 
      "ancestry": "dwarf" 
    }
  },
  "Layla": { 
    "character": { 
      "name": "Lira Thistlefoot", 
      "class": "rogue", 
      "ancestry": "halfling" 
    }
  }
}


Worldbuilder
You are a world-builder for a dungeons and dragons table top role playing game. You are responsible for creating places and characters in the present and in the past. When you create characters and places in the past you must ensure story continuity. your response must always be a json formatted output. Start with a new context that will be used for the opening scene of the game. Include enough information to enable a narrator to create an interesting scene

{
  "scene": {
    "setting": {
      "location": "Vyrnmoor",
      "description": "Nestled in a mist-laden valley between jagged mountains, Vyrnmoor is a mysterious town surrounded by ancient, towering trees and endless fields of wild heather. Its streets are narrow and winding, with homes and shops built of dark timber, weathered stone, and roofs made of green mossy slate. Faint traces of fog cling to every corner, giving the town a perpetually ethereal and haunting appearance. Strange runes are carved into the buildings’ stones, remnants of a time long forgotten."
    },
    "time_of_day": "Twilight",
    "weather": {
      "description": "A thin veil of mist rolls through the town, thickening as dusk approaches. The air is cool and damp, with a light drizzle adding to the already ominous ambiance. Low rumbles of thunder can be heard in the distance, hinting at a storm brewing far off in the mountains."
    },
    "historical_context": {
      "recent_past": "Vyrnmoor has only recently emerged from a long period of isolation. For decades, the town was cut off from neighboring cities after a series of brutal storms and landslides buried all trade routes leading out. Only recently, a strange mage known as Irenos, 'The Stormbreaker,' arrived and carved through the mountainside, reopening the path to the outside world. Since then, trade has resumed, and rumors of buried treasure from the old days have drawn adventurers to the town.",
      "ancient_past": "Centuries ago, Vyrnmoor was a sacred site for the order of the Veilkeepers, a now-vanished sect devoted to safeguarding secrets of the arcane. They built their monastery at the edge of the town, which still stands today as the Shrouded Sanctum, a ruin tangled in vines and largely abandoned. Legends say the Veilkeepers performed a mysterious ritual there to seal away 'The Whispering Ones,' a group of ancient beings capable of warping reality with their voices. The ritual supposedly failed, leaving a dark stain on the land that can still be felt by those with magic sensitivity."
    }
  },
  "characters": [
    {
      "name": "Irenos the Stormbreaker",
      "race": "Half-Elf",
      "class": "Wizard",
      "description": "A mysterious figure, Irenos is tall and lean, with long silver hair that falls around his shoulders like a cascade of mist. His eyes are a piercing shade of icy blue, and he wears a robe embroidered with cloud and lightning motifs. He carries a staff crowned with a crystal that appears to hold a swirling storm within it.",
      "background": "Irenos arrived in Vyrnmoor a year ago, claiming he had 'seen' the buried paths in a vision. After using his magic to clear the way, he has since set up a workshop in an old tower on the outskirts of town. Some see him as a savior, while others view him with suspicion, fearing his motives are not as pure as he claims."
    },
    {
      "name": "Ealdred the Keeper",
      "race": "Human",
      "class": "Historian (NPC)",
      "description": "An elderly man with a thin frame and a soft, raspy voice, Ealdred is the town’s resident historian and one of the few people alive with knowledge of the Veilkeepers. His face is deeply lined, and his eyes are clouded with age, though they still burn with an intense curiosity. He wears a hooded, tattered cloak and carries an ancient tome bound in cracked leather.",
      "background": "Ealdred has lived in Vyrnmoor his entire life and has an intense fascination with its hidden history. He claims to have descended from the Veilkeepers themselves, although there’s no proof of this. He warns travelers of the Shrouded Sanctum’s dangers but is willing to share secrets about it for the right price."
    },
    {
      "name": "Mira Stonewhisper",
      "race": "Dwarf",
      "class": "Rogue",
      "description": "With a mane of dark curly hair and a hardened look in her eyes, Mira is a rogue who has recently taken up residence in Vyrnmoor. She has a jagged scar across her left cheek and wears a well-worn leather jacket covered in an assortment of stolen trinkets.",
      "background": "Rumored to be a treasure hunter, Mira has been asking about the Veilkeepers’ vaults and is frequently seen near the ruins of the Shrouded Sanctum. She is tight-lipped about her past but is always eager to learn of any secrets connected to the order."
    }
  ],
  "narrative_hooks": [
    {
      "description": "As the characters enter Vyrnmoor, they notice the people whispering and avoiding eye contact, casting wary glances at the encroaching mist as if fearful of what it might conceal."
    },
    {
      "description": "They come across Irenos in the town square, muttering about strange energy patterns coming from the Shrouded Sanctum. He stops to ask if they have come to seek the secrets of the Whispering Ones."
    },
    {
      "description": "The players overhear a heated conversation between Mira Stonewhisper and Ealdred the Keeper in a dimly lit tavern. Mira demands more information about the Veilkeepers' vaults, while Ealdred warns her about tampering with forces beyond her understanding."
    }
  ]
}



Here is the context of the opening scene. Please describe what the players characters can see, without providing any backstory. Then ask what they want to do.






History is a collection of events.
Each event involves a thing existing in a place at a time.

continent of treos emerged on planet in the beginning
place - continent of treos
in_place - planet
time - the beginning

Humans arrive on continent of treos 1 million years ago
thing - human ancestry
place - continent of treos
time - 1 million years ago


The martines region emerged in continent of treos in the beginning
place - martines region
in_place - continent of treos
time - the beginning


The Darson tribe emerged from human ancestry in martines region 5000 years ago
thing - Darson tribe
from_thing - human ancestry
place - martines region
time - 5000 years ago


The Partelle family emerged from the Darson tribe in the city of pargille 300 years ago
thing - Partelle family
from_thing - Darson tribe
place - pargille city
time - 300 years ago


The barlow suburb built in pargille city 500 years ago
place - barlow suburb
from_place - pargille city
time - 500 years ago


The barlow suburb has wealthy people 400 years ago
thing - wealthy people
place - barlow suburb
time - 500 years ago


Jeff was born to Partelle family in the Partelle estate 30 years ago
thing - Jeff
from_thing - Partelle family
place - Partelle estate
time - 30 years ago


pig and worm tavern was built in barlow suburb 100 years ago
thing - pig and worm tavern
time - 100 years ago


Jeff sitting in the pig and worm tavern now
thing - Jeff Partelle
place - pig and worm tavern
time - now


Context Query 
place - pig and worm tavern
time - now

result: Jeff, humans, wealthy people