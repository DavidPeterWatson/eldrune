import re
import json


def join_property(dict_list, property_name, separator=", "):
    return separator.join(str(d[property_name]) for d in dict_list)


def extract_json(response_text):

    json_pattern = r'\{.*?\}'
    match = re.search(json_pattern, response_text, re.DOTALL)
    
    if match:
        try:
            json_data = json.loads(match.group())
            return json_data
        except json.JSONDecodeError:
            print("Error: Found JSON structure, but couldn't decode.")
            return None
    else:
        print("No JSON-like structure found in response.")
        return None