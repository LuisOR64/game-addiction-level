import numpy as np
import torch
import torch.nn as nn # Necesario para la definición de la clase del modelo
import joblib # Necesario para cargar los escaladores

# --- Definición de la clase del modelo (copiada de celda ZKor7saP2DDX) ---
class Red_salud_mental(nn.Module):
    def __init__(self, input_dim):
        super(Red_salud_mental, self).__init__()
        self.capas = nn.Sequential(
            nn.Linear(input_dim, 16),
            nn.BatchNorm1d(16), # Batch Normalization
            nn.ReLU(),
            #nn.Dropout(0.3),
            nn.Linear(16, 32),
            #nn.Linear(input_dim, 16),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            #nn.Dropout(0.3),
            nn.Linear(32, 8),
            nn.BatchNorm1d(8),
            nn.ReLU(),
            #nn.Dropout(0.3),
            nn.Linear(8, 1)  # Output single value
        )

    def forward(self, x):
        return self.capas(x)
# --- Fin de la definición de la clase ---

# --- Configuración dinámica del hardware ---
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"🚀 Ejecutando inferencia en: {device.type.upper()}")

# --- Cargar los escaladores ---
scaler_X_cargado = joblib.load('escalador_X.pkl')
scaler_Y_cargado = joblib.load('escalador_Y.pkl')

# Determinar input_dimension desde el escalador cargado
input_dimension = scaler_X_cargado.n_features_in_

# Re-instanciar el modelo usando el input_dimension obtenido
modelo_cargado = Red_salud_mental(input_dimension)

# --- CARGA INTELIGENTE DE PESOS ---
# Usamos map_location=device para que asigne los pesos directamente al hardware activo
pesos = torch.load('modelo.pth', map_location=device)
modelo_cargado.load_state_dict(pesos)

# Mover la estructura completa del modelo al dispositivo (GPU/CPU)
modelo_cargado.to(device)
modelo_cargado.eval() # Poner el modelo en modo evaluación (desactiva BatchNorm/Dropout para testeo)
# --- Fin de la carga ---

# --- Datos de Entrada ---
# Ejemplo: Si input_dimension es 15, deberías tener 15 valores aquí.
random_input_data = np.array([[0.5, 0.2, 0.8, 0.1, 0.6, 0.3, 0.9, 0.4, 0.7, 0.05, 0.95, 0.15, 0.85, 0.25, 0.75]]) 

# Verificar que la dimensión de los datos ingresados coincide con la esperada
if random_input_data.shape[1] != input_dimension:
    raise ValueError(f"El número de características en random_input_data ({random_input_data.shape[1]}) no coincide con input_dimension ({input_dimension}).")

# Escalar los datos de entrada usando el escalador_X_cargado
scaled_random_input = scaler_X_cargado.transform(random_input_data)

# Convertir a tensor de PyTorch y mover de forma segura al hardware activo (GPU o CPU)
scaled_random_input_t = torch.FloatTensor(scaled_random_input).to(device)

# Realizar la predicción
with torch.no_grad():
    scaled_prediction = modelo_cargado(scaled_random_input_t)

# Importante: Bajamos la predicción a la CPU (.cpu()) antes de transformarla a NumPy
original_prediction = scaler_Y_cargado.inverse_transform(scaled_prediction.cpu().numpy())

# --- Resultados ---
print("\n--- RESULTADOS ---")
print("Datos de entrada (escala original):\n", random_input_data)
print("Predicción del nivel de adicción (escala original):\n", original_prediction)