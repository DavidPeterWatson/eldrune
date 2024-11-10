from src.tools import extract_json
import json

def test_extract_json():
    ai_response = 'saying: Fantastic! So we have your campaign ready. Here’s a summary of what we’ll be playing: ```json {"campaign_name": "Legends of the Lost Kingdom", "theme": "Epic quests", "setting": "Classic fantasy realms"}```'
    actual = extract_json(ai_response)
    expected = {"campaign_name": "Legends of the Lost Kingdom", "theme": "Epic quests", "setting": "Classic fantasy realms"}
    assert expected == actual

def test_extract_players_json():
    ai_response = 'Fantastic! Here is the compiled information in the requested format:\n\n```json\n{\n  "identified-players": {\n    "David": {\n      "character": {\n        "name": "Pak",\n        "class": "wizard",\n        "ancestry": "elf"\n      }\n    },\n    "Arya": {\n      "character": {\n        "name": "Dorian",\n        "class": "druid",\n        "ancestry": "unknown"\n      }\n    }\n  }\n}\n``` \n\nIf you need anything else or are ready to begin the adventure, just let me know!'
    actual = extract_json(ai_response)
    expected = {
            "identified-players": {
                "David": {
                    "character": {
                        "name": "Pak",
                        "class": "wizard",
                        "ancestry": "elf"
                    }
                },
                "Arya": {
                    "character": {
                        "name": "Dorian",
                        "class": "druid",
                        "ancestry": "unknown"
                    }
                }
            }
        }
    assert expected == actual

def test_extract_players_json_a():
    ai_response = '{ "identified-players": {"David": {"character": {"name": "Pak","class": "wizard","ancestry": "elf"} },"Arya": {"character": {"name": "Dorian","class": "druid","ancestry": "unknown"} } } }'
    actual = extract_json(ai_response)
    expected = {
            "identified-players": {
                "David": {
                    "character": {
                        "name": "Pak",
                        "class": "wizard",
                        "ancestry": "elf"
                    }
                },
                "Arya": {
                    "character": {
                        "name": "Dorian",
                        "class": "druid",
                        "ancestry": "unknown"
                    }
                }
            }
        }
    expected_str = json.dumps(expected)
    print(expected_str)
    assert expected == actual