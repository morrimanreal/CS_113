import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def load_dataset():
    try:
        data = pd.read_csv("example_data.csv")

        print("Dataset loaded successfully!")
        print()
        print(data)

        return data

    except FileNotFoundError:
        print("Error: CSV file was not found.")
        return None
    
    
def explore_data(data):
    print("\n--- Basic Statistics ---")

    # Displays count, mean, standard deviation,
    # minimum, maximum, and quartiles
    print(data.describe())


def visualize_data(data):
    # Create scatter plot
    plt.scatter(data["Size (sqft)"], data["Price ($)"])

    plt.title("House Size vs. Price")
    plt.xlabel("Size (sqft)")
    plt.ylabel("Price ($)")

    plt.show()
    
    
def train_model(data):
    # X = input/independent variable
    X = data[["Size (sqft)"]]

    # y = output/dependent variable
    y = data["Price ($)"]

    # Create linear regression model
    model = LinearRegression()

    # Train the model
    model.fit(X, y)

    # Display model information
    print("\n--- Linear Regression Model ---")
    print("Coefficient:", model.coef_[0])
    print("Intercept:", model.intercept_)
    print("R² Score:", model.score(X, y))

    return model


def main():
    dataset = load_dataset()
    
    if dataset is not None:
        explore_data(dataset)
        visualize_data(dataset)
        model = train_model(data)


main()