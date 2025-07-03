import numpy as np
from datetime import datetime

class GenCastModel:
    """Simple deterministic model for demonstration."""

    def predict(self, timestamp: datetime) -> dict:
        hour_angle = (timestamp.hour % 24) / 24 * 2 * np.pi
        temperature = 15 + 10 * np.sin(hour_angle)
        humidity = 60 + 10 * np.cos(hour_angle)
        return {
            "temperature": round(float(temperature), 2),
            "humidity": round(float(humidity), 2),
        }
