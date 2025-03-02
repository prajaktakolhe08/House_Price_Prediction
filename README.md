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

<table> <tr> <td width="65%"> <video src="https://github.com/user-attachments/assets/cd7ff379-0416-43f3-a2bf-bc1c22baec25" controls width="100%"></video> </td> <td width="35%"> The demo showcases: - 🏡 User Input Form: Users enter house features (e.g., area, bedrooms, condition, etc.), ⚡ Prediction Process: The model processes the input and predicts the house price, 📊 Result Display: The estimated house price is shown on the result screen, 🔄 Real-time Interaction: Users can modify inputs and get updated predictions instantly.</td> </tr> </table>

## Setup and Installation

Follow these steps to set up and run the project on your local machine
1. **Clone the Repository**
   Download the project by running:
   ```sh
   git clone https://github.com/prajaktakolhe08/House_Price_Prediction
   cd House_Price_Prediction
   ```

3. **Create a Virtual Environment (Recommended)**
   
   It’s best to use a virtual environment to manage dependencies. Run the following command:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate # For macOS/Linux
   ```

5. **Install Dependencies**
   
   Ensure all required packages are installed:
   ```sh
   pip install -r requirements.txt
   ```

7. **Run the Flask Application**
   
   Start the web application:
   ```sh
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000/`

## Usage
1. Open the web application in a browser.
2. Enter the required house features in the form.
3. Click the "Predict Price" button.
4. The predicted house price will be displayed on the results page.

## Screenshots

### 🏠 Form Submission
<img alt="Homepage" src="https://github.com/user-attachments/assets/e321b912-f73d-42dc-81f3-3b618722974c" width="500">

### 📊 Predicted Result
<img alt="Predicted_result" src="https://github.com/user-attachments/assets/14a5ff8a-95df-475f-8aec-e6539c54f14a" width="500">

## Contact

If you have any questions or would like to contribute, feel free to email me or connect with me on [Linkedin](https://linkedin.com/in/prajakta-kolhe08).

⭐ **If you like this project, don't forget to give it a star!** ⭐
