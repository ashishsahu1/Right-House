import json
import pickle
import numpy as np

__location = None
__data_columns = None
__model = None

def predict_price(location,sqft,bath,bhk): 
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

def getLocation():
    return __location

def loadArtifact():
    print("Loading saved artifacts..")
    global __location
    global __data_columns
    global __model
    
    with open("./servers/artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]

    with open("./servers/artifacts/banglore_home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts... done")

if __name__ == "__main__":
    loadArtifact()
    print(getLocation())
    print(predict_price('1st Phase JP Nagar',1000, 2, 2))
    print(predict_price('1st Phase JP Nagar',1000, 3, 3))
    print(predict_price('Indira Nagar',1000, 3, 3))