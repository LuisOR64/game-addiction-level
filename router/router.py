from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.game_addiction import Game_addiction
from models.game_addictionIA import Game_addictionIA
from driver.driver import get_db
from driver.driver import insert_gameAddictionLevel, list_gameAddictionLevel, search_gameAddictionLevel, update_gameAddictionLevel, delete_gameAddictionLevel, predict
from models.schemas import gameAddictionResp, gameAddictionPredict, gameAddictionMessegeResp, DEFAULT_MESSAGE

router = APIRouter(
    prefix="/Game_addiction",
    tags=["game_addiction"]
)

@router.post("/predict", response_model = gameAddictionPredict)
def game_addiction_IA(game_addictionIA: Game_addictionIA):
    game_addiction_level = predict(game_addictionIA)

    return {
        "age": game_addictionIA.age,
        "daily_gaming_hours": game_addictionIA.daily_gaming_hours,
        "weekly_sessions": game_addictionIA.weekly_sessions,
        "night_gaming_ratio": game_addictionIA.night_gaming_ratio,
        "weekend_gaming_hours": game_addictionIA.weekend_gaming_hours,
        "multiplayer_ratio": game_addictionIA.multiplayer_ratio,
        "toxic_exposure": game_addictionIA.toxic_exposure,
        "violent_games_ratio": game_addictionIA.violent_games_ratio,
        "microtransactions_spending": game_addictionIA.microtransactions_spending,
        "sleep_hours": game_addictionIA.sleep_hours,
        "caffeine_intake": game_addictionIA.caffeine_intake,
        "exercise_hours": game_addictionIA.exercise_hours,
        "screen_time_total": game_addictionIA.screen_time_total,
        "friends_gaming_count": game_addictionIA.friends_gaming_count,
        "online_friends": game_addictionIA.online_friends,
        "addiction_level": game_addiction_level
    }

@router.post("/", response_model = gameAddictionMessegeResp)
def make_game_addiction(data: Game_addictionIA, db: Session = Depends(get_db)):    
    game_addiction: Game_addiction = insert_gameAddictionLevel(data, db)
    return {
        "message": DEFAULT_MESSAGE["insert"],
        "obj": game_addiction
    }

@router.get("/", response_model = list[gameAddictionResp])
def get_list_game_addiction(db: Session = Depends(get_db)):
    return list_gameAddictionLevel(db)

@router.get("/{id}", response_model = gameAddictionResp)
def get_game_addiction_byid(id:int, db: Session = Depends(get_db)):
    return search_gameAddictionLevel(id, db)

@router.put("/{id}", response_model = gameAddictionMessegeResp)
def update_game_addiction_dat(id: int, data: Game_addictionIA, db: Session = Depends(get_db)):
    return {
        "message": DEFAULT_MESSAGE["update"],
        "obj": update_gameAddictionLevel(id, data, db)
    }

@router.delete("/{id}", response_model = gameAddictionMessegeResp)
def delete_game_addiction_dat(id: int, db: Session = Depends(get_db)):
    return {
        "message": DEFAULT_MESSAGE["delete"],
        "obj": delete_gameAddictionLevel(id, db)
    }
