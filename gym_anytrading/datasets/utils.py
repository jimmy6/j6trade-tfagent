import os
import pandas as pd


def load_dataset(name, index_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, 'data', name + '.csv')
    return pd.read_csv(path, index_col=index_name)

def load_j6_dataset(name):
    return pd.read_csv('C:\\workspace\\j6stock\\' + name + '.txt')