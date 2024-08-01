# model-visualizer
A web application that can produce different types of regression, classification, and clustering models depending on input. Users input a csv file and choose what kind of model they want to see. Their results will show in graph and numerical form.

Model Types:
- Linear Regression
- Multiple Linear Regression
- Polynomial Regression

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Naive Bayes

- K-Means Clustering  
- Hierarchical Clustering

Stack:
- Django
- React

ML Libraries:
- numpy
- matplotlib
- pandas
- sklearn

Process:
- input data in csv form
- preprocessing data
    - clean data + split training and test set
- choosing regression + classification + clustering w/ select dropdown
- choosing model w/ select dropdown
- display results onto frontend w/ React
    - accuracy + graph
    - use MongoDB to hold data for all models
- reset button? 

Goals:
- improve Django knowledge
- better understand how frontend and backend interact
