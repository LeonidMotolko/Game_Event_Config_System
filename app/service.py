import json
from textwrap import indent


def load_events():
    with open("configs/events.json", "r") as file:
        return json.load(file)


def get_event_by_id(event_id: int):
    events = load_events()
    for event in events:
        if event["id"] == event_id:
            return event
    return None


def check_event(event: dict, player_data: dict) -> bool:
    conditions = event.get("conditions", {})

    if "min_level" in conditions:
        if player_data.get("level", 0) < conditions["min_level"]:
            return False

    if "kills" in conditions:
        if player_data.get("kills", 0) < conditions["kills"]:
            return False

    return True


def save_events(events: list):
    with open("configs/events.json", "w", encoding="utf-8") as file:
        json.dump(events, file, indent = 2)


def update_event(event_id: int, new_data: dict):
    events = load_events()

    for event in events:
        if event["id"] == event_id:
            event.update(new_data)
            save_events(events)
            return event

    return None