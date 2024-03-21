import subprocess
import requests
import time

def test_docker():
    subprocess.Popen(['docker', 'run', '-d', '-p', '5000:5000', 'flask-app'])
    time.sleep(2)
    
    response = requests.post('http://localhost:5000', data={'text': 'Sample text'})
    assert response.status_code == 200

    subprocess.Popen(['docker', 'stop', '$(docker ps -q)'])
    subprocess.Popen(['docker', 'rm', '$(docker ps -a -q)'])
    subprocess.Popen(['docker', 'rmi', 'flask-app'])
    subprocess.Popen(['docker', 'image', 'prune', '-f'])

if __name__ == "__main__":
    test_docker()
