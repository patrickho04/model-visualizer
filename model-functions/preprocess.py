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

class Data():
    # Initizliaing input and output values of dataset
    def __init__(self, csv_file):                                   
        self.dataset = pd.read_csv(csv_file)
        self.X = self.dataset.iloc[:, :-1].values
        self.Y = self.dataset.iloc[:, -1].values
    
    # Encoding data
    def encode_data() -> None:
        pass
    
    # Take care of missing data (replace w/ avg)
    def replace_missing_data(self, lower: int, upper: int, type: str = 'mean') -> None:
        imputer = SimpleImputer(missing_values=np.nan, strategy=type)
        imputer.fit(self.X[:, lower:upper])
        self.X[:, lower:upper] = imputer.transform(self.X[:, lower:upper])
    
    # Spliting dataset into training and test
    def split_train_test_sets(self) -> None:
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.X, self.Y, test_size = 1/3)

# Testing
test = Data('Data.csv')
print(test.X)
print("\n")
test.replace_missing_data(lower=2, upper=3, type='median')
print(test.X)

