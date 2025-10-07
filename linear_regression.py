import numpy as np
from sklearn.linear_model import LinearRegression

def generate_data(n_points, slope, intercept, noise_level):
    """
    Generates synthetic data for a simple linear regression problem.

    Args:
        n_points (int): The number of data points to generate.
        slope (float): The slope of the true underlying line.
        intercept (float): The intercept of the true underlying line.
        noise_level (float): The standard deviation of the Gaussian noise to add.

    Returns:
        tuple: A tuple containing the features (X) and the target (y) as numpy arrays.
    """
    # Generate X values uniformly from 0 to 10
    X = np.random.rand(n_points, 1) * 10
    
    # Generate Gaussian noise
    noise = np.random.randn(n_points, 1) * noise_level
    
    # Generate y values using the linear equation y = a*X + b + noise
    y = slope * X + intercept + noise
    
    return X, y

def train_model(X, y):
    """
    Trains a simple linear regression model on the given data.

    Args:
        X (np.array): The input features.
        y (np.array): The target values.

    Returns:
        LinearRegression: The trained scikit-learn LinearRegression model.
    """
    # Create a Linear Regression model instance
    model = LinearRegression()
    
    # Fit the model to the data
    model.fit(X, y)
    
    return model

# This block runs only when the script is executed directly
if __name__ == '__main__':
    # --- Configuration for a test run ---
    n_points = 100
    true_slope = 2.5
    true_intercept = 5
    noise_level = 2

    print("--- Generating Test Data ---")
    # Generate synthetic data using the specified parameters
    X_test, y_test = generate_data(n_points, true_slope, true_intercept, noise_level)
    print(f"Generated {len(X_test)} data points.")

    print("\n--- Training Model ---")
    # Train a linear regression model on the generated data
    trained_model = train_model(X_test, y_test)
    print("Model training complete.")

    print("\n--- Model Results ---")
    # Print the learned parameters of the model
    print(f"Original Slope: {true_slope}")
    print(f"Model's Learned Slope (Coefficient): {trained_model.coef_[0][0]:.4f}")
    print(f"Original Intercept: {true_intercept}")
    print(f"Model's Learned Intercept: {trained_model.intercept_[0]:.4f}")