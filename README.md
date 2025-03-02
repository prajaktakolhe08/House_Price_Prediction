# 🏡 House Price Prediction Web Application

## Overview
This project is a House Price Prediction Web Application built with Flask and a pre-trained machine learning model. Users can input various house features such as area, overall quality, number of bathrooms, and other attributes, and the application predicts the estimated house price using a Random Forest model. The interactive web interface provides an intuitive way to explore real estate pricing trends based on input data.

## Features
- User-friendly web interface for inputting house details
- Predicts house prices based on key features such as Lot Area, Overall Quality, Year Built, etc.
- Utilizes a trained Random Forest model for accurate predictions
- Displays the predicted house price on a results page

## Technologies Used
- **Flask**: Web framework for handling routes and rendering templates
- **Jupyter Notebook**: Used for exploratory data analysis and model training
- **Scikit-learn**: Used for training and deploying the Random Forest model
- **Joblib**: Model serialization for loading the trained model
- **Pandas**: Data manipulation and preprocessing
- **HTML/CSS**: Frontend for user input and result display

## Demo

- House Price Prediction Demo
&nbsp
<table> <tr> <td width="65%"> <video src="https://github.com/user-attachments/assets/ca219045-c9ce-4970-bb8c-ef573d739489" controls width="100%"></video> </td> <td width="35%"> The demo showcases: - 🏡 User Input Form: Users enter house features (e.g., area, bedrooms, condition, etc.), ⚡ Prediction Process: The model processes the input and predicts the house price, 📊 Result Display: The estimated house price is shown on the result screen, 🔄 Real-time Interaction: Users can modify inputs and get updated predictions instantly.</td> </tr> </table>

## Project Structure
```
project-directory/
│-- model/
│   ├── house_price_rf_model.pkl  # Trained model file
|-- dataset/ 
|-- |── train.csv # Dataset used for training
|   |── test.csv
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
   git clone https://github.com/prajaktakolhe08House_Price_Prediction
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

## Contact

If you have any questions or would like to contribute, feel free to email me or connect with me on [Linkedin](https://linkedin.com/in/prajakta-kolhe08).

⭐ **If you like this project, don't forget to give it a star!** ⭐
