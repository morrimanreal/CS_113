import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset from a CSV file
def load_dataset():
    try:
        data = pd.read_csv("house-prices.csv")

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

    # Displays mean, min, max, standard deviation, etc.
    print(data[["SqFt", "Price"]].describe())

    # Display individual statistics
    print("\nAverage House Size:", data["SqFt"].mean())
    print("Minimum House Size:", data["SqFt"].min())
    print("Maximum House Size:", data["SqFt"].max())

    print("\nAverage Price: $", data["Price"].mean())
    print("Minimum Price: $", data["Price"].min())
    print("Maximum Price: $", data["Price"].max())

    # Scatter plot
    plt.scatter(data["SqFt"], data["Price"])

    plt.xlabel("House Size (SqFt)")
    plt.ylabel("House Price ($)")
    plt.title("House Size vs. Price")

    plt.show()

# Visualize the relationship between house size and price
def visualize_data(data):
    # House size
    X = data[["SqFt"]]

    # Actual house prices
    y = data["Price"]

    # Get predicted prices
    predicted_prices = model.predict(X)

    # Plot actual data points
    plt.scatter(data["SqFt"], y, label="Actual Prices")

    # Plot regression line
    plt.plot(data["SqFt"], predicted_prices, label="Regression Line")

    # Add graph labels
    plt.xlabel("House Size (SqFt)")
    plt.ylabel("House Price ($)")
    plt.title("House Size vs. Price")

    plt.legend()
    plt.show()
    
# Train a linear regression model to predict house prices based on size    
def train_model(data):
    # Independent variable
    X = data[["SqFt"]]

    # Dependent variable
    y = data["Price"]

    # Create model
    model = LinearRegression()

    # Train model
    model.fit(X, y)

    # Calculate R-squared
    r_squared = model.score(X, y)

    print("\n--- Linear Regression Model ---")

    print("Coefficient:", model.coef_[0])
    print("Intercept:", model.intercept_)
    print("R² Score:", r_squared)

    return model

# Visualize the model's predictions against actual data
def visualize_model(data, model):
    # Independent variable
    X = data[["SqFt (SqFt)"]]

    # Actual house prices
    y = data["Price ($)"]

    # Predict prices using the trained model
    predicted_prices = model.predict(X)

    # Plot original data points
    plt.scatter(data["SqFt (SqFt)"], y, label="Actual Prices")

    # Plot regression line
    plt.plot(data["SqFt (SqFt)"], predicted_prices,
             label="Regression Line")

    # Labels and title
    plt.xlabel("SqFt (SqFt)")
    plt.ylabel("Price ($)")
    plt.title("House Size vs. Price")

    plt.legend()
    plt.show()
    
# Predict house price based on user input    
def predict_price(model):
    while True:
        try:
            # Ask user for house size
            size = float(input("\nEnter house size in square feet: "))

            # Check for negative or zero values
            if size <= 0:
                print("House size must be greater than 0.")
                continue

            # Put user input into a DataFrame
            house = pd.DataFrame({
                "SqFt": [size]
            })

            # Predict house price
            prediction = model.predict(house)

            # Display predicted price
            print(f"Estimated House Price: ${prediction[0]:,.2f}")

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