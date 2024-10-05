from django.urls import path
from .views import allergy_prediction

urlpatterns = [
    path('predict/', allergy_prediction, name='allergy_prediction'),
]
