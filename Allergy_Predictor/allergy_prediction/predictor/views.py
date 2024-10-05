from django.shortcuts import render
from .forms import AllergyForm
from .models import Allergy
import joblib
import pandas as pd
import os
from django.shortcuts import redirect

# Load the model and feature names globally
model = joblib.load(os.path.join(os.path.dirname(__file__), 'allergy_model.pkl'))
feature_names = model.feature_names_in_

def home(request):
    return redirect('allergy_prediction')  # Redirect to the allergy prediction page

def allergy_prediction(request):
    if request.method == 'POST':
        form = AllergyForm(request.POST)
        if form.is_valid():
            # Prepare data for prediction
            input_data = {
                'IgE Levels (kU/L)': form.cleaned_data['ige_levels'],
                'Exposure Frequency': form.cleaned_data['exposure_frequency'],
                'Allergen Type': form.cleaned_data['allergen_type'],
                'Symptoms': form.cleaned_data['symptoms'],
                'Family History': form.cleaned_data['family_history']
            }

            # Load the model
            #model = joblib.load('allergy_model.pkl')

            # Create a DataFrame for prediction
            df_input = pd.DataFrame([input_data])
            df_input = pd.get_dummies(df_input)

            # Align columns with the model's expected input
            df_input = df_input.reindex(columns=feature_names, fill_value=0)

            # Predict
            prediction = model.predict(df_input)
            reaction_severity = prediction[0]

            # Save user input to the database
            allergy_instance = Allergy(
                allergen_type=form.cleaned_data['allergen_type'],
                ige_levels=form.cleaned_data['ige_levels'],
                exposure_frequency=form.cleaned_data['exposure_frequency'],
                symptoms=form.cleaned_data['symptoms'],
                family_history=form.cleaned_data['family_history'],
                reaction_severity=reaction_severity
            )
            allergy_instance.save()

            return render(request, 'predictor/result.html', {'reaction_severity': reaction_severity})
    else:
        form = AllergyForm()

    return render(request, 'predictor/predict.html', {'form': form})
