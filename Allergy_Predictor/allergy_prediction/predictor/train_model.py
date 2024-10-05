import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    # Load dataset
    df = pd.read_csv('C:/Users/prince_singh04/OneDrive/Desktop/Allergy_Predictor/allergy_prediction/allergy_data.csv')  

    # Prepare features and labels
    X = df[['IgE Levels (kU/L)', 'Exposure Frequency', 'Allergen Type', 'Symptoms', 'Family History']]
    y = df['Reaction Severity']

    # Encode categorical variables
    X = pd.get_dummies(X, columns=['Exposure Frequency', 'Allergen Type', 'Symptoms', 'Family History'])

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, 'allergy_model.pkl')
    return model.feature_names_in_

if __name__ == '__main__':
    train_model()
