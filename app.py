import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import plotly.graph_objects as go

# Import the data generation and model training functions from our other script
from linear_regression import generate_data, train_model

# --- Page Configuration ---
# Set the title and a short description for the web app
st.title("Simple Linear Regression Explorer")
st.write("""
This application demonstrates a simple linear regression model.
You can control the data generation process using the sliders in the sidebar,
and the app will train a model and visualize the results in real-time.
""")

# --- Sidebar for User Inputs ---
# Create a sidebar for all the user-adjustable parameters
st.sidebar.header("Data Generation Parameters")

# Sliders to control the data generation
n_points = st.sidebar.slider("Number of data points:", min_value=5, max_value=500, value=100, step=5)
slope = st.sidebar.slider("Slope (a) of the true line:", min_value=-10.0, max_value=10.0, value=2.5, step=0.1)
intercept = st.sidebar.slider("Intercept (b) of the true line:", min_value=-10.0, max_value=10.0, value=5.0, step=0.1)
noise_level = st.sidebar.slider("Amount of random noise:", min_value=0.0, max_value=10.0, value=2.0, step=0.1)

# --- Core Application Logic ---

# 1. Generate the synthetic data based on user inputs
X, y = generate_data(n_points, slope, intercept, noise_level)
# Create a pandas DataFrame for easier handling and display
df = pd.DataFrame({'X': X.flatten(), 'y': y.flatten()})

# 2. Train the linear regression model on the generated data
model = train_model(X, y)
# Get the predictions from the trained model
y_pred = model.predict(X)

# 3. Evaluate the model's performance
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

# --- Display Results in the Main Panel ---

st.header("Model Results")

# Display the evaluation metrics in two columns
col1, col2 = st.columns(2)
col1.metric("Mean Squared Error (MSE)", f"{mse:.2f}")
col2.metric("R-squared (R²)", f"{r2:.2f}")

# Display the visualization of the data and model
st.header("Data Visualization")

# Create a Plotly figure
fig = go.Figure()

# Add a scatter plot of the generated data points
fig.add_trace(go.Scatter(x=df['X'], y=df['y'], mode='markers', name='Generated Data'))

# Add the fitted regression line from the model
fig.add_trace(go.Scatter(x=X.flatten(), y=y_pred.flatten(), mode='lines', name='Fitted Regression Line', line=dict(color='red')))

# Add the original "true" line for comparison
true_y = slope * X.flatten() + intercept
fig.add_trace(go.Scatter(x=X.flatten(), y=true_y, mode='lines', name='True Line', line=dict(color='green', dash='dash')))

# Update the layout of the plot
fig.update_layout(
    title="Linear Regression Fit",
    xaxis_title="X-axis",
    yaxis_title="y-axis"
)

# Render the plot in the Streamlit app
st.plotly_chart(fig)

# Display the raw generated data in a table
st.header("Generated Data")
st.dataframe(df)