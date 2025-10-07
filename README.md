# Simple Linear Regression Explorer

This is a simple web application built with Streamlit that allows users to explore the concepts of simple linear regression.

## Features

-   Generate synthetic data with customizable parameters (slope, intercept, noise).
-   Train a simple linear regression model on the generated data.
-   Visualize the data, the true underlying line, and the fitted regression line.
-   View model performance metrics (Mean Squared Error and R-squared).

## Project Structure

-   `app.py`: The main Streamlit application file.
-   `linear_regression.py`: A module containing the core logic for data generation and model training.
-   `requirements.txt`: A list of Python dependencies for the project.
-   `Todo.md`: The project execution log.
-   `original_project_plan.md`: The initial high-level project plan.
-   `modified_project_plan.md`: The detailed project execution plan.

## How to Run the Application

1.  **Clone the repository or download the project files.**

2.  **Set up a Python virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

5.  **Open your web browser** and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).
