from fastapi import FastAPI
from app.service import load_events, get_event_by_id, check_event
from app.service import update_event

app = FastAPI()


@app.get("/events")
def get_events():
    return load_events()


@app.post("/check-event/{event_id}")
def check_event_for_player(event_id: int, player: dict):
    event = get_event_by_id(event_id)

    if not event:
        return {"error": "Event not found"}

    result = check_event(event, player)

    return {
        "event": event["name"],
        "completed": result
    }

@app.put("/event/{event_id}")
def update_event_endpoint(event_id: int, new_data: dict):
    updated_event = update_event(event_id, new_data)

    if not updated_event:
        return {"error": "Event not found"}

    return {
        "message": "Event updated successfully",
        "event": updated_event
    }