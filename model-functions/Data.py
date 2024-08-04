# import and clean data
# encode data (category vs numerical)
# each dataset is a class?
    # variables for dataset, X, Y


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

class Data():
    # Initizliaing input and output values of dataset
    def __init__(self, csv_file: str):                                   
        self.dataset = pd.read_csv(csv_file)
        self.X = self.dataset.iloc[:, :-1].values
        self.Y = self.dataset.iloc[:, -1].values    

    # Take care of missing data (replace w/ avg)    
    def replace_missing_data(self, lower: int, upper: int, type: str = 'mean') -> None:
        imputer = SimpleImputer(missing_values=np.nan, strategy=type)
        imputer.fit(self.X[:, lower:upper])
        self.X[:, lower:upper] = imputer.transform(self.X[:, lower:upper])
    
    # One Hot Encoder (1,0,0; 0,1,0; 0,0,1; etc.)
    def one_hot_encode(self, lower: int, upper: int) -> None:
        ct = ColumnTransformer(transformers=[('encode', OneHotEncoder(), [i for i in range(lower, upper)])], remainder='passthrough')
        self.X = np.array(ct.fit_transform(self.X))
    
    # Label Encoder (for dependent variables w/ binary values)
    def label_encode(self) -> None:
        le = LabelEncoder()
        self.Y = le.fit_transform(self.Y)

    # Spliting dataset into training and test
    def create_train_test_sets(self, size: float) -> None:
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.X, self.Y, test_size = size, random_state=1)
    
    # Scale features (always split first)
    def standardization(self, lower: int, upper: int) -> None:
        sc = StandardScaler()
        self.x_train[:, lower:upper] = sc.fit_transform(self.x_train[:, lower:upper])
        self.x_test[:, lower:upper] = sc.transform(self.x_test[:, lower:upper]) 
