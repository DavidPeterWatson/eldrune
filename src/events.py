from enum import StrEnum

class PlaceScale(StrEnum):
    # Macro-Scale
    # PLANE = "PLANE"  # The world or overarching plane of existence
    WORLD = "WORLD"  # The world or overarching plane of existence. 36 000 kilometers
    CONTINENT = "Continent"  # Large landmasses or divisions. 5000 kilometers
    REALM = "Realm"  # Broad regions like kingdoms or natural zones. 1000 kilometers

    # Mid-Scale
    TERRITORY = "Territory"  # Sub-regions like provinces or territories, Mountain range, Large Forest. 100 kilometers
    DOMAIN = "Domain"  # Towns, cities, or significant settlements, Mountain, forest. 10 Kilometers
    DISTRICT = "District"  # Subdivisions of towns or cities or sides of a mountain, region of forest. 1 kilometer

    # Micro-Scale
    SITE = "Site"  # Key locations within districts like a tavern, a castle, a dungeon, or a temple, glade, dungeon. 100 meters
    CHAMBER = "Chamber"  # Specific rooms or areas within sites. 10 meters
    SPOT = "Spot"  # Character-level scale, actual spot. 1 meter


class TimeScale(StrEnum):
    # Macro-Scale
    EON = "Eon"  # Grandest spans of time, entire ages or epochs. 1 billion years
    ERA = "Era"  # Significant periods marked by major shifts. 100 million years
    # EPOCH = "Epoch"  # Subdivisions of eras, often regional or cultural. 10 million years
    AGE = 'Age' # 1 Million years

    # Mid-Scale
    MILLENNIUM = 'Millennium' # 1000 years. 1000 per age
    CENTURY = "Century"  # Hundred-year spans, major developments. 
    YEAR = "Year"  # Single year, tied to calendars or events, integer year of century 100

    # Micro-Scale
    DAY = "Day"  # Single day, significant for short-term events, Day of season
    MOMENT = "Moment"  # Smallest measurable unit, immediate action. time of day

class SubjectScale(StrEnum):
    # Broadest Level
    ANCESTRY = "Ancestry"  # Broadest lineage, encompassing entire races or species (e.g., "Elves," "Dragons")
    TRIBE = "Tribe"  # Subdivisions of ancestry, such as familial or noble lineages (e.g., "House of Sylvaris")
    CLAN = "Clan"  # Smaller familial or tribal groups within a bloodline (e.g., "Stonehammer Clan")
    FAMILY = "Family"  # Immediate familial unit, including extended family (e.g., "The Thornroot Family")
    INDIVIDUAL = "Individual" 

# class Place():
#     def __init__(self, name: str, description: str, place_scale: PlaceScale, encompassing_place: str):
#         self.name = name
#         self.description = description
#         self.place_scale = place_scale
#         self.encompassing_place = encompassing_place


# class Period():
#     def __init__(self, name: str, description: str, period_scale: TimeScale, encompassing_period: str):
#         self.period_scale = period_scale
#         self.encompassing_period = encompassing_period


# class Subject():
#     def __init__(self, name: str, description: str, encompassing_subject: str):
#         self.place_scale = time_scale
#         self.encompassing_time = encompassing_time



# class Event():
#     def __init__(self, place: Place, period: Period):
#         self.place = place
#         self.period = period