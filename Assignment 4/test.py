# import subprocess
# import requests
# import time
# import os
# os.chdir("Assignment 4")

# def test_docker():
#     # Build Docker image
#     subprocess.run(['docker', 'build', '-t', 'spam-classifier', '.'])
#     subprocess.Popen(['docker', 'run', '-d', '-p', '5000:5000', 'spam-classifier'])
#     time.sleep(2)
    
#     response = requests.post('http://localhost:5000', data={'text': 'Sample text'})
#     assert response.status_code == 200

#     container_id = subprocess.check_output(['docker', 'ps', '-q'], text=True).strip()
#     subprocess.Popen(['docker', 'stop', container_id])

# if __name__ == "__main__":
#     test_docker()


# import os
# import requests
# import time
# import subprocess

# def test_docker():
#     # Build Docker image
#     subprocess.run(['docker', 'build', '-t', 'spam-classifier', 'Assignment 4'])

#     # Run Docker container
#     docker_run_process = subprocess.Popen(['docker', 'run', '-d', '-p', '5000:5000', 'spam-classifier'])

#     # Allow some time for the container to start
#     time.sleep(2)

#     try:
#         # Send a request to the /score endpoint
#         response = requests.post('http://localhost:5000', data={'text': 'Your sample text here'})

#         # Check if the response is as expected
#         if response.status_code == 200:
#             print("Response:", response.json())
#             # Add your assertions here to check the response content

#     finally:
#         # Close the Docker container
#         subprocess.run(['docker', 'stop', docker_run_process.stdout.decode().strip()])




# import os
# import subprocess
# import requests
# import time


# def test_docker():
    
    
#     # Build the Docker image
#     subprocess.run(["docker", "build", "-t", "spam-classifier", "Assignment 4"])

#     # Run the Docker container
#     subprocess.run(["docker", "run", "-d", "-p", "5000:5000", "--name", "spam-container", "spam-classifier"])

#     # Send a request to the localhost endpoint /score
#     response = requests.post("http://localhost:5000", data={"text": "sample_text"}, timeout=20)

#     # Check if the response is as expected
#     assert response.status_code == 200

#     # Close the Docker container
#     subprocess.run(["docker", "stop", "spam-container"])
#     subprocess.run(["docker", "rm", "spam-container"])
#     subprocess.run(["docker", "rmi", "spam-classifier"])

# if __name__ == "__main__":
#     test_docker()



import time
import requests
import subprocess

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
        # Send a request to the container
        response = requests.post("http://localhost:5000", data={"text": "sample_text"}, timeout=10)

        # Check if the response is as expected
        assert response.status_code == 200

    # Close the Docker container
    subprocess.run(["docker", "stop", "spam-container"])
    subprocess.run(["docker", "rm", "spam-container"])
    subprocess.run(["docker", "rmi", "spam-classifier"])

if __name__ == "__main__":
    test_docker()
