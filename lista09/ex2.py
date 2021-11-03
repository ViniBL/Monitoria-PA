import json
def is_json(string):
    try:
        json.loads(string)
        return True
    except json.JSONDecodeError:
        return False


