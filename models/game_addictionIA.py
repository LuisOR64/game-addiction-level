from pydantic import BaseModel, Field
from typing import Literal

class Game_addictionIA(BaseModel):
    age: float = Field(ge = 0)
    daily_gaming_hours: float = Field(ge = 0)
    weekly_sessions: float = Field(ge = 0)
    night_gaming_ratio: float = Field(ge = 0)
    weekend_gaming_hours: float = Field(ge = 0)
    multiplayer_ratio: float = Field(ge = 0)
    toxic_exposure: float = Field(ge = 0)
    violent_games_ratio: float = Field(ge = 0)
    microtransactions_spending: float = Field(ge = 0)
    sleep_hours: float = Field(ge = 0)
    caffeine_intake: float = Field(ge = 0)
    exercise_hours: float = Field(ge = 0)
    screen_time_total: float = Field(ge = 0)
    friends_gaming_count: float = Field(ge = 0)
    online_friends: float = Field(ge = 0)