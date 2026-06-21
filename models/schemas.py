from pydantic import BaseModel, Field

DEFAULT_MESSAGE = {
    "insert": "Complete, Game addiction level was inserted",
    "update": "Complete, Game addiction level was updated",
    "delete": "Complete, Game addiction level was deleted"
}

class gameAddictionPredict(BaseModel):
    age: float
    daily_gaming_hours: float
    weekly_sessions: float
    night_gaming_ratio: float
    weekend_gaming_hours: float
    multiplayer_ratio: float
    toxic_exposure: float
    violent_games_ratio: float
    microtransactions_spending: float
    sleep_hours: float
    caffeine_intake: float
    exercise_hours: float
    screen_time_total: float
    friends_gaming_count: float
    online_friends: float
    addiction_level: float

class gameAddictionResp(BaseModel):
    id: int
    age: float
    daily_gaming_hours: float
    weekly_sessions: float
    night_gaming_ratio: float
    weekend_gaming_hours: float
    multiplayer_ratio: float
    toxic_exposure: float
    violent_games_ratio: float
    microtransactions_spending: float
    sleep_hours: float
    caffeine_intake: float
    exercise_hours: float
    screen_time_total: float
    friends_gaming_count: float
    online_friends: float
    addiction_level: float

class gameAddictionMessegeResp(BaseModel):
    message: str
    obj: gameAddictionResp