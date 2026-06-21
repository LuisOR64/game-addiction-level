from driver.driver_db import SessionLocal
from sqlalchemy.orm import Session
from models.game_addiction import Game_addiction
from models.game_addictionIA import Game_addictionIA
from model_ia.model import predict

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def gameAddictionLevel_constructor(data: Game_addictionIA) -> Game_addiction:
    return Game_addiction(
        age = float(data.age),
        daily_gaming_hours = float(data.daily_gaming_hours),
        weekly_sessions = float(data.weekly_sessions),
        night_gaming_ratio = float(data.night_gaming_ratio),
        weekend_gaming_hours = float(data.weekend_gaming_hours),
        multiplayer_ratio = float(data.multiplayer_ratio),
        toxic_exposure = float(data.toxic_exposure),
        violent_games_ratio = float(data.violent_games_ratio),
        microtransactions_spending = float(data.microtransactions_spending),
        sleep_hours = float(data.sleep_hours),
        caffeine_intake = float(data.caffeine_intake),
        exercise_hours = float(data.exercise_hours),
        screen_time_total = float(data.screen_time_total),
        friends_gaming_count = float(data.friends_gaming_count),
        online_friends = float(data.online_friends)
    )

def list_gameAddictionLevel(db: Session):
    return db.query(Game_addiction).all()

def search_gameAddictionLevel(id: int, db: Session):
    game_addiction: Game_addiction = db.query(Game_addiction).filter(Game_addiction.id == id).first()

    if not game_addiction:
        game_addiction = Game_addiction()

    return game_addiction

def insert_gameAddictionLevel(data: Game_addictionIA, db: Session):
    addict_prediction = predict(data)

    game_addiction = gameAddictionLevel_constructor(data)
    game_addiction.addiction_level = addict_prediction
    
    db.add(game_addiction)
    db.commit()
    db.refresh(game_addiction)

    return game_addiction

def update_gameAddictionLevel(id: int, data: Game_addictionIA, db: Session):
    game_addiction: Game_addiction = db.query(Game_addiction).filter(Game_addiction.id == id).first()
    
    if game_addiction:
        
        addict_prediction = predict(data)

        game_addiction.age = data.age
        game_addiction.daily_gaming_hours = data.daily_gaming_hours
        game_addiction.weekly_sessions = data.weekly_sessions
        game_addiction.night_gaming_ratio = data.night_gaming_ratio
        game_addiction.weekend_gaming_hours = data.weekend_gaming_hours
        game_addiction.multiplayer_ratio = data.multiplayer_ratio
        game_addiction.toxic_exposure = data.toxic_exposure
        game_addiction.violent_games_ratio = data.violent_games_ratio
        game_addiction.microtransactions_spending = data.microtransactions_spending
        game_addiction.sleep_hours = data.sleep_hours
        game_addiction.caffeine_intake = data.caffeine_intake
        game_addiction.exercise_hours = data.exercise_hours
        game_addiction.screen_time_total = data.screen_time_total
        game_addiction.friends_gaming_count = data.friends_gaming_count
        game_addiction.online_friends = data.online_friends
        game_addiction.addiction_level = addict_prediction

        db.commit()
        db.refresh(game_addiction)
    else:
        game_addiction = Game_addiction()
    
    return game_addiction

def delete_gameAddictionLevel(id: int, db: Session):
    game_addiction: Game_addiction = db.query(Game_addiction).filter(Game_addiction.id == id).first()

    if game_addiction:
        db.delete(game_addiction)
        db.commit()
    else:
        game_addiction = Game_addiction()

    return game_addiction