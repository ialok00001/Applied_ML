import pytest
from score import score
import pickle
import warnings
warnings.filterwarnings("ignore")


model = pickle.load(open("Assignment 3/model.pkl", "rb"))


def test_smoke_test():
    try:
        score("Example", model, 0.5)
    except Exception as e:
        pytest.fail(f"score function raised an exception: {e} (Smoke test failed)")
    
    assert type(score("Example", model, 0.5)) == tuple, f"Expected 2 outputs, received 1 (smoke test failed)"
    assert len(score("Example", model, 0.5)) == 2, f"Expected 2 outputs, received {len(score('Example', model, 0.5))} (smoke test failed)"

def test_format_test():
    text = "Example"
    threshold = 0.7
    prediction, probability = score(text, model, threshold)
    assert type(prediction) == int
    
    try:
        float(probability)
    except Exception as e:
        pytest.fail(f"score function raised an exception: {e} (Format test failed)")

def test_prediction_0_or_1():
    text = "Example"
    threshold = 0.7
    prediction, _ = score(text, model, threshold)
    assert prediction in (0, 1)

def test_propensity_between_0_and_1():
    text = "Example"
    threshold = 0.7
    _, propensity = score(text, model, threshold)
    assert 0<=propensity<=1

def test_when_threshold_0_prediction_always_1():
    text_1 = "Be there tonight"
    threshold = 0
    prediction, _ = score(text_1, model, threshold)
    assert prediction == 1
    
    text_2 = "Get a chance to go on a vacation to Hawaii"
    threshold = 0
    prediction, _ = score(text_2, model, threshold)
    assert prediction == 1

def test_when_threshold_1_prediction_always_0():
    text_1 = "Be there tonight"
    threshold = 1
    prediction, _ = score(text_1, model, threshold)
    assert prediction == 0
    
    text_2 = "Get a chance to go on a vacation to Hawaii"
    threshold = 1
    prediction, _ = score(text_2, model, threshold)
    assert prediction == 0

def test_obvious_spam_gives_prediction_1():
    text = '''Just apply to this lucky draw and get a chance to send
              your child to foreign universities like Stanford and Harvard. Don't be late. 
              Offer valid for a limited time only.'''
    threshold = 0.7
    prediction, _ = score(text, model, threshold)
    assert prediction == 1

def test_obvious_non_spam_gives_prediction_0():
    text = "Don't be late for tomorrow's meeting"
    threshold = 0.4
    prediction, _ = score(text, model, threshold)
    assert prediction == 0