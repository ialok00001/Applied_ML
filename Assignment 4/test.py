import subprocess
import requests
import time

def test_docker():
    # Launch Docker container
    subprocess.Popen(['docker', 'run', '-d', '-p', '5000:5000', 'flask-app'])
    time.sleep(2)  # Allow time for container to start
    
    # Send request to localhost endpoint
    response = requests.post('http://localhost:5000', data={'text': 'Sample text'})
    
    # Check if response is as expected
    assert response.status_code == 200
    # Add more assertions as needed
    
    # Stop Docker container
    subprocess.Popen(['docker', 'stop', '$(docker ps -q)'])

    # Optionally, you can also remove the stopped containers
    subprocess.Popen(['docker', 'rm', '$(docker ps -a -q)'])

    # Optionally, you can also remove the built image
    subprocess.Popen(['docker', 'rmi', 'flask-app'])

    # Optionally, you can also remove dangling images
    subprocess.Popen(['docker', 'image', 'prune', '-f'])

if __name__ == "__main__":
    test_docker()
