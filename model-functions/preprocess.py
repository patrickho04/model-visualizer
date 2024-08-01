# import and clean data
# encode data (category vs numerical)
# each dataset is a class?
    # variables for dataset, X, Y


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

class Data():
    # Initizliaing input and output values of dataset
    def __init__(self, csv_file):                                   
        self.dataset = pd.read_csv(csv_file)
        self.X = self.dataset.iloc[:, :-1].values
        self.Y = self.dataset.iloc[:, -1].values
    
    # Spliting dataset into training and test
    def split_train_test_sets(self):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.X, self.Y, test_size = 1/3)
    
    # Encoding data
    
        

test = Data('Data.csv')
test.split_train_test_sets()
print(test.x_test)
