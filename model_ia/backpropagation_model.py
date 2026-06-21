import torch.nn as nn

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