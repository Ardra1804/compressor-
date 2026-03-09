from src.excel_parser import parse_excel
from src.feature_engineering import calculate_features
from src.normalization import normalize_metrics
from src.ahp_weights import get_weights
from src.ranking_engine import rank_machines

def run_pipeline(file):

    df = parse_excel(file)

    print("Parsed data:")
    print(df)
    df = calculate_features(df)

    print("\nAfter feature engineering:")
    print(df)

    metrics = [
        "sec",
        "leakage",
        "fad_efficiency",
        "pressure_stability",
        "velocity_uniformity",
        "running_stability"
    ]

    scaled = normalize_metrics(df, metrics)

    weights = get_weights()

    scores = rank_machines(scaled, metrics, weights)

    df["performance_score"] = scores

    return df.sort_values("performance_score", ascending=False)