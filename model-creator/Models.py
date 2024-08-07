from Data import Data
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# test manipulating data in and outside function

def linear_regression_model(ds: Data):
    # Linear regression model
    regressor = LinearRegression()
    regressor.fit(ds.x_train, ds.y_train)
    y_pred = regressor.predict(ds.x_test)

    # Plotting line against training input
    plt.scatter(ds.x_train, ds.y_train, color='red')
    plt.plot(ds.x_train, regressor.predict(ds.x_train), color='blue')
    plt.title('Salary vs. Experience (Training Set)')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.show()

    # Plotting line against test set
    plt.scatter(ds.x_test, ds.y_test, color='red')
    plt.plot(ds.x_train, regressor.predict(ds.x_train), color='blue')
    plt.title('Salary vs. Experience (Test Set)')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.show()

test = Data('Salary_Data.csv')
test.create_train_test_sets(0.2)
linear_regression_model(test)