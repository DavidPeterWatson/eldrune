import re
import json
import string


def join_property(dict_list, property_name, separator=", "):
    return separator.join(str(d[property_name]) for d in dict_list)


def extract_json(response_text):
    cleaned_text = response_text.replace("\n", "")
    start = "```json"
    end = "```"

    if start in cleaned_text:
        try:
            substr = cleaned_text[cleaned_text.index(start) + len(start):]
            substr = substr[:substr.index(end)]
            json_data = json.loads(substr)
            return json_data
        except json.JSONDecodeError:
            print("Error: Found JSON structure, but couldn't decode.")
            return None
    else:
        try:
            json_data = json.loads(cleaned_text)
            return json_data
        except json.JSONDecodeError:
            print("No JSON-like structure found in response.")
            return None
