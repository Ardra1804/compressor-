from src.excel_parser import parse_velocity_sheet
from src.feature_engineering import calculate_features
from src.normalization import normalize_metrics
from src.ahp_weights import get_weights
from src.ranking_engine import rank_machines

df = parse_velocity_sheet("data/raw_excel/machine_dataset.xlsx")

df = calculate_features(df)

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

result = rank_machines(scaled, metrics, weights)

print(result)