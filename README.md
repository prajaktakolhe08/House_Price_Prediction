# 🏡 House Price Prediction Web Application

## Overview
This project is a House Price Prediction Web Application built using Flask and a pre-trained machine learning model. The application takes various house features as input and predicts the estimated price of the house using a Random Forest model.

## Features
- User-friendly web interface for inputting house details
- Predicts house prices based on key features such as Lot Area, Overall Quality, Year Built, etc.
- Utilizes a trained Random Forest model for accurate predictions
- Displays the predicted house price on a results page

## Technologies Used
- **Flask**: Web framework for handling routes and rendering templates
- **Scikit-learn**: Used for training and deploying the Random Forest model
- **Joblib**: Model serialization for loading the trained model
- **NumPy**: Data processing and transformation
- **HTML/CSS**: Frontend for user input and result display

## Project Structure
```
project-directory/
│-- model/
│   ├── house_price_rf_model.pkl  # Trained model file
|-- dataset/ 
|-- |── train.csv # Dataset used for training
    |── test.csv
|-- static/
│   ├── style.css 
│-- templates/
│   ├── index.html  # Form for user input
│   ├── result.html  # Displays predicted price
│-- app.py  # Flask application file
│-- requirements.txt  # List of dependencies
│-- README.md  # Documentation
```

## Setup and Installation
1. **Clone the Repository**
   ```sh
   git clone <repository_url>
   cd project-directory
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Flask Application**
   ```sh
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000/`

## Usage
1. Open the web application in a browser.
2. Enter the required house features in the form.
3. Click the "Predict Price" button.
4. The predicted house price will be displayed on the results page.
