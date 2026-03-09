import numpy as np

def calculate_features(df):

    # FAD efficiency
    if "actual_fad" in df.columns and "rated_fad" in df.columns:
        df["fad_efficiency"] = df["actual_fad"] / df["rated_fad"]
    else:
        df["fad_efficiency"] = 0

    # pressure stability
    if "unload_pressure" in df.columns and "load_pressure" in df.columns:
        df["pressure_stability"] = df["unload_pressure"] - df["load_pressure"]
    else:
        df["pressure_stability"] = 0

    # velocity uniformity
    velocity_cols = [c for c in df.columns if c.startswith("v")]

    if velocity_cols:
        df["velocity_uniformity"] = df[velocity_cols].std(axis=1)
    else:
        df["velocity_uniformity"] = 0

    # running stability
    if "running_time" in df.columns and "loading_time" in df.columns:
        df["running_stability"] = df["running_time"] / df["loading_time"]
    else:
        df["running_stability"] = 0

    return df