import numpy as np
import torch
#import torch.nn as nn
import joblib
from model_ia.backpropagation_model import Red_salud_mental
from models.game_addictionIA import Game_addictionIA

def make_input(age:float, daily_gaming_hours:float, weekly_sessions:float, night_gaming_ratio:float, weekend_gaming_hours:float, multiplayer_ratio:float, toxic_exposure:float, violent_games_ratio:float, microtransactions_spending:float, sleep_hours:float, caffeine_intake:float, exercise_hours:float, screen_time_total:float, friends_gaming_count:float, online_friends:float) -> dict:
    return {
        "age":age, 
        "daily_gaming_hours":daily_gaming_hours, 
        "weekly_sessions":weekly_sessions, 
        "night_gaming_ratio":night_gaming_ratio, 
        "weekend_gaming_hours":weekend_gaming_hours, 
        "multiplayer_ratio":multiplayer_ratio, 
        "toxic_exposure":toxic_exposure, 
        "violent_games_ratio":violent_games_ratio, 
        "microtransactions_spending":microtransactions_spending, 
        "sleep_hours":sleep_hours, 
        "caffeine_intake":caffeine_intake, 
        "exercise_hours":exercise_hours, 
        "screen_time_total":screen_time_total, 
        "friends_gaming_count":friends_gaming_count, 
        "online_friends":online_friends
    }

def predict(data:Game_addictionIA) -> float:
    
    input_data = np.array([[data.age, data.daily_gaming_hours, data.weekly_sessions, data.night_gaming_ratio, data.weekend_gaming_hours, data.multiplayer_ratio, data.toxic_exposure, data.violent_games_ratio, data.microtransactions_spending, data.sleep_hours, data.caffeine_intake, data.exercise_hours, data.screen_time_total, data.friends_gaming_count, data.online_friends]])
    #input_data = np.array([[data["age"], data["daily_gaming_hours"], data["weekly_sessions"], data["night_gaming_ratio"], data["weekend_gaming_hours"], data["multiplayer_ratio"], data["toxic_exposure"], data["violent_games_ratio"], data["microtransactions_spending"], data["sleep_hours"], data["caffeine_intake"], data["exercise_hours"], data["screen_time_total"], data["friends_gaming_count"], data["online_friends"]]])
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    scaler_X_cargado = joblib.load('model_ia/model/escalador_X.pkl')
    scaler_Y_cargado = joblib.load('model_ia/model/escalador_Y.pkl')

    input_dimension = scaler_X_cargado.n_features_in_

    modelo_cargado = Red_salud_mental(input_dimension)

    pesos = torch.load('model_ia/model/modelo.pth', map_location=device)
    modelo_cargado.load_state_dict(pesos)

    modelo_cargado.to(device)
    modelo_cargado.eval()

    if input_data.shape[1] != input_dimension:
        raise ValueError(f"El número de características en input_data ({input_data.shape[1]}) no coincide con input_dimension ({input_dimension}).")

    scaled_random_input = scaler_X_cargado.transform(input_data)

    scaled_random_input_t = torch.FloatTensor(scaled_random_input).to(device)

    with torch.no_grad():
        scaled_prediction = modelo_cargado(scaled_random_input_t)

    original_prediction = scaler_Y_cargado.inverse_transform(scaled_prediction.cpu().numpy())

    return float(original_prediction.item())