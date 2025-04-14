import pandas as pd

def load_disease_info():
    return pd.read_csv("data/diseases.csv")
