from score import score
import pickle
import time
import requests
import subprocess
import os
import warnings
warnings.filterwarnings("ignore")


model = pickle.load(open("Assignment 4/model.pkl", "rb"))


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



def test_flask():

    process = subprocess.Popen(["python", "Assignment 4/app.py"], stdout=subprocess.PIPE)

    time.sleep(2)

    payload = {"text": "Hello, congratulations! You have won a prize."}
    response = requests.post("http://localhost:5000/", data=payload)

    assert response.status_code == 200

    data = response.json()
    assert 'prediction' in data
    assert 'propensity' in data

    process.terminate()



def wait_for_container_ready():
    max_retries = 10
    retry_delay = 5  # seconds

    for _ in range(max_retries):
        try:
            # Send a test request to the container to check if it's ready
            response = requests.post("http://localhost:5000", data={"text": "sample_text"}, timeout=2)
            if response.status_code == 200:
                print("Container is ready")
                return True
        except Exception as e:
            print(f"Error checking container status: {e}")

        print("Container is not ready yet, retrying...")
        time.sleep(retry_delay)

    print("Max retries exceeded, container is not ready")
    return False

def test_docker():
    # Build the Docker image
    subprocess.run(["docker", "build", "-t", "spam-classifier", "Assignment 4"])

    # Run the Docker container
    subprocess.run(["docker", "run", "-d", "-p", "5000:5000", "--name", "spam-container", "spam-classifier"])

    # Wait for the container to be ready
    if wait_for_container_ready():
        print("Test passed!")
        with open(os.path.join("Assignment 4", "test_results.txt"), "a") as f:
            f.write("Test passed!\n")
    else:
        print("Test failed!")
        with open(os.path.join("Assignment 4", "test_results.txt"), "a") as f:
            f.write("Test failed!\n")

    # Close the Docker container
    subprocess.run(["docker", "stop", "spam-container"])
    subprocess.run(["docker", "rm", "spam-container"])
    subprocess.run(["docker", "rmi", "spam-classifier"])

if __name__ == "__main__":
    test_docker()
