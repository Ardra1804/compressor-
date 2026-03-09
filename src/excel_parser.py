import pandas as pd
import re

def clean(text):
    if pd.isna(text):
        return ""
    return str(text).strip().lower()

def parse_excel(file):

    df = pd.read_excel(file, header=None)

    # ---- detect machine row ----
    machine_row = None

    for i in range(len(df)):
        row = df.iloc[i].apply(clean)

        if any("ac" in cell for cell in row):
            machine_row = i
            break

    if machine_row is None:
        raise ValueError("Machine names not found.")

    machines = df.iloc[machine_row, 1:].dropna().tolist()
    machine_cols = df.iloc[machine_row, 1:].dropna().index.tolist()

    # ---- find parameter rows ----
    params = {}

    for i in range(len(df)):

        label = clean(df.iloc[i, 0])

        if "fad capacity" in label:
            params["rated_fad"] = i

        elif "actual fad" in label:
            params["actual_fad"] = i

        elif "leakage" in label:
            params["leakage"] = i

        elif "sec" in label or "specific energy" in label:
            params["sec"] = i

        elif "loading pressure" in label:
            params["load_pressure"] = i

        elif "unloading pressure" in label:
            params["unload_pressure"] = i

        elif "running time" in label:
            params["running_time"] = i

        elif "loading time" in label:
            params["loading_time"] = i

    # ---- detect velocity rows ----
    velocity_rows = []

    for i in range(len(df)):
        label = clean(df.iloc[i, 0])

        if re.search(r"velocity\s*v\d+", label):
            velocity_rows.append(i)

    # ---- extract machine data ----
    records = []

    for col, machine in zip(machine_cols, machines):

        row_data = {"machine": machine}

        for p, r in params.items():
            row_data[p] = df.iloc[r, col]

        for idx, r in enumerate(velocity_rows):
            row_data[f"v{idx+1}"] = df.iloc[r, col]

        records.append(row_data)

    dataset = pd.DataFrame(records)

    # ---- convert numbers ----
    for col in dataset.columns:
        if col != "machine":
            dataset[col] = pd.to_numeric(dataset[col], errors="coerce")

    return dataset