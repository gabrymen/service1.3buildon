import pickle
import pandas as pd
from sklearn.cluster import KMeans
from app import create_app

def load_model():
    with open('app/models/cluster_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model

def cluster_data(data):
    #model = load_model()
    #df = pd.DataFrame(data)
    #clusters = model.predict(df)
    #return clusters.tolist() 
    return ({"message": "Risposta Funzione cluster_data"})

