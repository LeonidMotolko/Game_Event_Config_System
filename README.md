# 🎮 LiveOps Event System (FastAPI)

A simple backend service that simulates a LiveOps event system used in online games.  
The project demonstrates how in-game events can be configured, activated, and filtered based on player data.

---

## 🚀 Features

- Config-driven event system (JSON-based)
- Time-based event activation
- Player-based event filtering (level, kills, wins)
- Simple and extensible conditions system
- REST API built with FastAPI

---

## 🧠 Concept

This project is inspired by LiveOps systems used in games like World of Tanks.

Events are:
- Defined in configuration (JSON)
- Activated within a time range
- Filtered based on player stats

---

## 📦 Tech Stack

- Python
- FastAPI
- JSON (config storage)

---

## 📁 Project Structure
game-event-system/
│
├── app/
│   ├── main.py
│   ├── service.py
│
├── configs/
│   └── events.json
│
├── README.md
├── requirements.txt

---

## ⚙️ Setup & Run

### 1. Install dependencies

```bash
pip install fastapi uvicorn
```
### 2.Run the srever

```bash
uvicorn main:app --reload
```

### 3. Open in browser
http://127.0.0.1:8000/docs

---

## 🔌 API Endpoints

### 📌 Get available events for player
#### POST /player-events

#### Request

```json
{
  "level": 6,
  "kills": 15,
  "wins": 2
}
```

#### Response

```json
{
  "available_events": [
    {
      "id": 1,
      "name": "Double XP Weekend"
    }
  ]
}
```

---

## 📄 Event Example (events.json)

```json
{
  "id": 1,
  "name": "Double XP Weekend",
  "start": "2026-04-01",
  "end": "2026-04-03",
  "conditions": {
    "min_level": 5,
    "kills": 10
  }
}
```

