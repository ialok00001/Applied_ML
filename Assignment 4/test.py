import subprocess
import requests
import time

def test_docker():
    subprocess.Popen(['docker', 'run', '-d', '-p', '5000:5000', 'flask-app'])
    time.sleep(2)  # Allow time for container to start
    
    response = requests.post('http://localhost:5000', data={'text': 'Sample text'})
    
    assert response.status_code == 200
    
    subprocess.Popen(['docker', 'stop', '$(docker ps -q)'])

if __name__ == "__main__":
    test_docker()
