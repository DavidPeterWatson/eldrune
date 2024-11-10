from src.tools import extract_json


def test_extract_json():
    ai_response = 'saying: Fantastic! So we have your campaign ready. Here’s a summary of what we’ll be playing: ```json {"campaign-name": "Legends of the Lost Kingdom", "theme": "Epic quests", "setting": "Classic fantasy realms"}```'
    actual = extract_json(ai_response)
    expected = {"campaign-name": "Legends of the Lost Kingdom", "theme": "Epic quests", "setting": "Classic fantasy realms"}
    assert expected == actual