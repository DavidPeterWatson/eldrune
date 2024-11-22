from src.memory import Memory
from src.events import TimeScale, PlaceScale, SubjectScale

def test_create_world():
    with Memory('tests') as memory:
        place_memory = memory.place_memory
        place_memory.forget_all_places()
        durnst = place_memory.remember_place({'name': 'Durnst', 'scale': PlaceScale.WORLD})
        recalled_durnst = place_memory.recall_place('Durnst')
        place_memory.forget_all_places()
        assert recalled_durnst == durnst
    
def test_create_continent():
    with Memory('tests') as memory:
        place_memory = memory.place_memory
        place_memory.forget_all_places()
        durnst = place_memory.remember_place({'name': 'Durnst', 'scale': PlaceScale.WORLD})
        antaria = place_memory.remember_place({'name': 'Antaria', 'scale': PlaceScale.CONTINENT, 'encompassing_place': 'Durnst'})
        recalled_antaria = place_memory.recall_place('Antaria')
        place_memory.forget_all_places()
        assert recalled_antaria == antaria
    

def test_get_context():
    memory = Memory('tests')
    place_memory = memory.place_memory
    event_memory = memory.event_memory
    
    durnst = place_memory.remember_place({'name': 'Durnst', 'scale': PlaceScale.WORLD})
    antaria = place_memory.remember_place({'name': 'Antaria', 'scale': PlaceScale.CONTINENT, 'encompassing_place': 'Durnst'})
    planc = place_memory.remember_place({'name': 'Planc', 'scale': PlaceScale.REALM, 'encompassing_place': 'Antaria'})
    dornhelm = place_memory.remember_place({'name': 'Dornhelm', 'scale': PlaceScale.REALM, 'encompassing_place': 'Planc'})

    gods = memory.remember_subject({'name': 'gods', 'scale': SubjectScale.ANCESTRY})
    the_creator = memory.remember_subject({'name': 'The creator', 'scale': SubjectScale.INDIVIDUAL, 'encompassing_subject':gods})

    creation_eon = memory.remember_time({'name': 'Creation Eon', 'scale': TimeScale.EON, 'number': 1})
    abandoned_eon = memory.remember_time({'name': 'Abandoned Eon', 'scale': TimeScale.EON, 'number': 3})
    era_of_shadows = memory.remember_time({'name': 'Era of Shadows', 'scale': TimeScale.ERA, 'encompassing_period': abandoned_eon, 'number': 6})
    age_of_the_first_flame = memory.remember_time({'name': 'Age of the First Flame', 'scale': TimeScale.AGE, 'encompassing_period': era_of_shadows, 'number': 10})
    tribal_years = memory.remember_time({'name': 'Tribal Years', 'scale': TimeScale.MILLENNIUM, 'encompassing_period': era_of_shadows })
    slavery_century = memory.remember_time({'name': 'slavery', 'scale': TimeScale.CENTURY, 'encompassing_period': tribal_years })
    year_of_liberation = memory.remember_time({'name': 'Liberation', 'scale': TimeScale.YEAR, 'encompassing_period': slavery_century })
    rise_of_humanity = memory.remember_time({'name': 'rise of humanity', 'scale': TimeScale.CENTURY, 'encompassing_period': tribal_years })
    year_of_darkness = memory.remember_time({'name': 'darkness', 'scale': TimeScale.YEAR, 'encompassing_period': rise_of_humanity })

    humans = memory.remember_subject({'name': 'humans', 'scale': SubjectScale.ANCESTRY})
    elves = memory.remember_subject({'name': 'elves', 'scale': SubjectScale.ANCESTRY})
    high_mage_elves = memory.remember_subject({'name': 'high mage elves', 'scale': SubjectScale.CLAN, 'encompassing_subject': elves})

    creation = event_memory.remember_event({'period': creation_eon, 'place': durnst, 'subjects': [the_creator], 'description': 'durnst is created by the creator god'})
    
    arrival_of_humans = event_memory.remember_event({'period': age_of_the_first_flame, 'place': antaria, 'subjects': [humans, high_mage_elves], 'description': 'Humans are first created by the high mage elves of Antaria as slaves'})
    humans_learn_magic = event_memory.remember_event({'period': age_of_the_first_flame, 'place': antaria, 'subjects': [humans, high_mage_elves], 'description': 'Humans learn magic in secret'})
    human_liberation = event_memory.remember_event({'period': age_of_the_first_flame, 'place': planc, 'subjects': [humans, high_mage_elves], 'description': 'Humans use magic skills to liberate themselves from elven dominion'})

    dwarves = memory.remember_subject({'name': 'dwarves', 'scale': SubjectScale.ANCESTRY})
    arrival_of_dwarves = event_memory.remember_event({'period': abandoned_eon, 'place': dornhelm, 'subjects': [dwarves, the_creator], 'description': 'Dwarves are first created by the creator god in Dornhelm'})

    actual_context = memory.get_context(planc, year_of_darkness)
    expected_context = [arrival_of_humans, humans_learn_magic, human_liberation]

    assert actual_context == expected_context

    memory.forget_all_places()


