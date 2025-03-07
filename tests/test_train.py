import pytest
import joblib
from src.train import model

def test_model_training():
    assert model is not None  # Ensure model is trained

def test_model_prediction():
    test_data = [[1, 0, 50000, 30, 0, 1, 20000, 2]]
    prediction = model.predict(test_data)
    assert prediction is not None  # Ensure model makes predictions
