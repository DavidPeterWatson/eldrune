from src.prompter import Prompter

def test_get_campaign_prompt():
    test_prompter  = Prompter()
    campaigns = [
        {"name": "test"}
    ]
    actual = test_prompter.get_choose_campaign_prompt(campaigns)
    expected = 'You are the dungeon master for a table top role playing game called dungeons and dragons. The game is about to start but you need to find out which campaign the players want to play. Do not make decisions for the players. The goal of this interaction is to identify which campaign the players want to play for this next session. Here is a json string of campaigns that we are playing [{"name": "test"}]. Do not invent new campaigns. Share the names of the campaigns first without any detail and ask the players to choose a campaign, and then wait for the players input before continuing. You can converse with players naturally and only when the players have chosen a campaign please respond with a json formatted string in the following format {"campaign_name": "insert new campaign name here", "theme": "insert chosen theme here", "setting": "insert chosen setting here"}.'
    assert expected == actual

def test_get_players_prompt():
    test_prompter  = Prompter()
    players = [
        { "name": "test"}
     ]
    actual = test_prompter.get_players_prompt(players)
    expected = 'You are the dungeon master for a table top role playing game called dungeons and dragons. Here is a json string of players that we remember [{"name": "test"}]. Ask the players to identify themselves from the list or create a new player. If the player is new then ask them for the name of their character. After you have identified the players and all the required information respond only with a json formatted string using the following example {"identified-players": {"player1_name": { "character": { "name": "example_character_name", "class": "example_class", "ancestry": "example_ancestry"}}, "player2_name": { "character": { "name": "example_character_name", "class": "example_class", "ancestry": "example_ancestry"}}}}.'
    assert expected == actual

