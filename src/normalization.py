from sklearn.preprocessing import MinMaxScaler

def normalize_metrics(df, metrics):

    scaler = MinMaxScaler()

    data = df[metrics].copy()

    for col in metrics:

        if data[col].max() == data[col].min():
            data[col] = 1   # identical values
        else:
            data[[col]] = scaler.fit_transform(data[[col]])

    return data