import json
import pickle

__locations = None
__data_columns = None
__model = None

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        data = json.load(f)
        __data_columns = data['availability_columns'] + data['area_columns'] + data['location_columns']
        __locations = data['location_columns']

    global __model
    if __model is None:
        with open("./artifacts/banglore_home_prices_model.pickle", "rb") as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = [0] * len(__data_columns)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)
