import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset from a CSV file
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
    
# Explore the dataset and display basic statistics    
def explore_data(data):
    print("\n--- Basic Statistics ---")

    # Displays count, mean, standard deviation,
    # minimum, maximum, and quartiles
    print(data.describe())

# Visualize the relationship between house size and price
def visualize_data(data):
    # Create scatter plot
    plt.scatter(data["Size (sqft)"], data["Price ($)"])

    plt.title("House Size vs. Price")
    plt.xlabel("Size (sqft)")
    plt.ylabel("Price ($)")

    plt.show()
    
# Train a linear regression model to predict house prices based on size    
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

# Visualize the model's predictions against actual data
def visualize_model(data, model):
    # Independent variable
    X = data[["Size (sqft)"]]

    # Actual house prices
    y = data["Price ($)"]

    # Predict prices using the trained model
    predicted_prices = model.predict(X)

    # Plot original data points
    plt.scatter(data["Size (sqft)"], y, label="Actual Prices")

    # Plot regression line
    plt.plot(data["Size (sqft)"], predicted_prices,
             label="Regression Line")

    # Labels and title
    plt.xlabel("Size (sqft)")
    plt.ylabel("Price ($)")
    plt.title("House Size vs. Price")

    plt.legend()
    plt.show()
    
# Predict house price based on user input    
def predict_price(model):
    while True:
        try:
            size = float(input("Enter house size in square feet: "))

            if size <= 0:
                print("House size must be greater than 0.")
                continue

            prediction = model.predict([[size]])

            print("Estimated house price: $", round(prediction[0], 2))

            break

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    dataset = load_dataset()
    
    if dataset is not None:
        explore_data(dataset)
        visualize_data(dataset)
        model = train_model(dataset)
        visualize_model(dataset, model)
        predict_price(model)


main()