import subprocess
import requests
import time

def test_docker():
    subprocess.Popen(['docker', 'run', '-d', '-p', '5000:5000', 'flask-app'])
    time.sleep(2)
    
    response = requests.post('http://localhost:5000', data={'text': 'Sample text'})
    assert response.status_code == 200

    container_id = subprocess.check_output(['docker', 'ps', '-q'], text=True).strip()
    subprocess.Popen(['docker', 'stop', container_id])

if __name__ == "__main__":
    test_docker()
