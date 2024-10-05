from django import forms

class AllergyForm(forms.Form):
    allergen_type = forms.ChoiceField(choices=[
        ('Food - Wheat', 'Food - Wheat'),
        ('Food - Nuts', 'Food - Nuts'),
        ('Food - Dairy', 'Food - Dairy'),
        ('Food - Seafood', 'Food - Seafood'),
        ('Environmental - Pollen', 'Environmental - Pollen'),
        ('Environmental - Dust', 'Environmental - Dust'),
        ('Environmental - Mold', 'Environmental - Mold'),
        ('Environmental - Insect', 'Environmental - Insect'),
        ('Food - Spices', 'Food - Spices'),
    ])
    ige_levels = forms.FloatField(label='IgE Levels (kU/L)')
    exposure_frequency = forms.ChoiceField(choices=[
        ('Rarely', 'Rarely'),
        ('Monthly', 'Monthly'),
        ('Daily', 'Daily'),
        ('Seasonal', 'Seasonal'),
    ])
    symptoms = forms.ChoiceField(choices=[
        ('Oral allergy syndrome', 'Oral allergy syndrome'),
        ('Swelling', 'Swelling'),
        ('Hives', 'Hives'),
        ('Itchy skin', 'Itchy skin'),
        ('Nasal congestion', 'Nasal congestion'),
        ('Coughing', 'Coughing'),
        ('Shortness of breath', 'Shortness of breath'),
        ('Rash', 'Rash'),
        ('Anaphylaxis', 'Anaphylaxis'),
    ])
    family_history = forms.ChoiceField(choices=[
        ('Yes', 'Yes'),
        ('No', 'No'),
    ])
