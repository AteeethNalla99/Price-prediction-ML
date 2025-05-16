import pickle
import json
import numpy as np
import pandas as pd

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    location = location.strip().lower()

    # Find location index by case-insensitive matching
    loc_index = -1
    for i, col in enumerate(__data_columns):
        if col.lower() == location:
            loc_index = i
            break

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    x_df = pd.DataFrame([x], columns=__data_columns)
    return round(__model.predict(x_df)[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    with open("./artifacts/columns.json", "r") as f:
        data_columns = json.load(f)['data_columns']
        # Instead of .title(), keep original casing from JSON or fix casing to match your model
        # Assuming columns.json now contains correct casing matching the model
        __data_columns = data_columns
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    if __model is None:
        with open('./artifacts/Bengaluru_House_Data.pickle', 'rb') as f:
            __model = pickle.load(f)

    print("loading saved artifacts...done")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st phase jp nagar', 1000, 3, 3))
    print(get_estimated_price('1st phase jp nagar', 1000, 2, 2))
    print(get_estimated_price('kalhalli', 1000, 2, 2))  # other location
    print(get_estimated_price('ejipura', 1000, 2, 2))   # other location
