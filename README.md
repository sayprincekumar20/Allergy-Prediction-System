# Allergy Prediction System
## Overview
The Allergy Prediction System is an end-to-end application developed in Django that predicts allergy reaction severity based on various factors, including IgE levels, exposure frequency, allergen type, symptoms, and family history. This project utilizes a Random Forest Classifier trained on a dataset to provide accurate predictions.

## Table of Contents
*     Features
      Technologies Used
      Installation
      Usage
      Dataset
      Model Training
      License
### Features
* Predicts the severity of allergic reactions.
* User-friendly web interface for data input.
* Utilizes a trained Random Forest model for accurate predictions.
* Easy to extend and modify for additional features.
### Technologies Used
* Django: Web framework for building the application.
* Pandas: Data manipulation and analysis.
* Scikit-learn: Machine learning library for model training and evaluation.
* Joblib: For saving and loading the trained model.
* HTML/CSS: Frontend for user interaction.
* 
### Usage
Train the Model: Run the following command to train the model and save it:


*     python train_model.py
This will create a file named allergy_model.pkl that contains the trained model.

Run the Django Application: Start the Django development server:

bash
                                              Copy code
*        python manage.py runserver
Access the Application: Open a web browser and navigate to http://127.0.0.1:8000/allergy/predict/ to use the application.

Dataset
The project uses a dataset named allergy_data.csv, which contains the following features:

IgE Levels (kU/L): The level of Immunoglobulin E in the blood.
Exposure Frequency: How often the individual is exposed to allergens.
Allergen Type: The type of allergen.
Symptoms: Symptoms experienced by the individual.
Family History: Family history of allergies.
Reaction Severity: The target variable indicating the severity of the reaction.
Model Training
The train_model.py script performs the following:

Loads the dataset from a CSV file.
Prepares features (X) and labels (y).
Encodes categorical variables using one-hot encoding.
Splits the data into training and testing sets.
Trains a Random Forest Classifier model on the training data.
Saves the trained model to a file named allergy_model.pkl.
Code Example
Here’s a brief snippet of the training code:

python
Copy code
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    df = pd.read_csv('C:/Users/prince_singh04/OneDrive/Desktop/Allergy_Predictor/allergy_prediction/allergy_data.csv')  
    X = df[['IgE Levels (kU/L)', 'Exposure Frequency', 'Allergen Type', 'Symptoms', 'Family History']]
    y = df['Reaction Severity']
    X = pd.get_dummies(X, columns=['Exposure Frequency', 'Allergen Type', 'Symptoms', 'Family History'])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, 'allergy_model.pkl')
License
This project is licensed under the MIT License. See the LICENSE file for details.
