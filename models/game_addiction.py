from sqlalchemy import Column, Integer, Float, String, Boolean
from driver.driver_db import Base

class Game_addiction(Base):
    __tablename__ = "game_addiction"
    
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Float, nullable=False)
    daily_gaming_hours = Column(Float, nullable=False)
    weekly_sessions = Column(Float, nullable=False)
    night_gaming_ratio = Column(Float, nullable=False)
    weekend_gaming_hours = Column(Float, nullable=False)
    multiplayer_ratio = Column(Float, nullable=False)
    toxic_exposure = Column(Float, nullable=False)
    violent_games_ratio = Column(Float, nullable=False)
    microtransactions_spending = Column(Float, nullable=False)
    sleep_hours = Column(Float, nullable=False)
    caffeine_intake = Column(Float, nullable=False)
    exercise_hours = Column(Float, nullable=False)
    screen_time_total = Column(Float, nullable=False)
    friends_gaming_count = Column(Float, nullable=False)
    online_friends = Column(Float, nullable=False)
    addiction_level = Column(Float, nullable=False)