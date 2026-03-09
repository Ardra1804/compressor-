import numpy as np

def get_weights():
    weights = {
        "sec":0.40,
        "leakage":0.20,
        "fad_efficiency":0.15,
        "pressure_stability":0.10,
        "velocity_uniformity":0.10,
        "running_stability":0.05
    }
    return weights