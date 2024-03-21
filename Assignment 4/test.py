# import subprocess
# import requests
# import time

# def test_docker():
#     subprocess.Popen(['docker', 'run', '-d', '-p', '5000:5000', 'flask-app'])
#     time.sleep(2)
    
#     response = requests.post('http://localhost:5000', data={'text': 'Sample text'})
#     assert response.status_code == 200

#     subprocess.Popen(['docker', 'stop', '$docker ps -q'])
#     # subprocess.Popen(['docker', 'rm', '$(docker ps -a -q)'])
#     # subprocess.Popen(['docker', 'rmi', 'flask-app'])
#     # subprocess.Popen(['docker', 'image', 'prune', '-f'])

# if __name__ == "__main__":
#     test_docker()




import subprocess
import requests
import time

def test_docker():
    # Start the Docker container
    subprocess.Popen(['docker', 'run', '-d', '-p', '5000:5000', 'flask-app'])
    time.sleep(2)  # Wait for the container to start
    
    # Make a request to the containerized Flask app
    response = requests.post('http://localhost:5000', data={'text': 'Sample text'})
    assert response.status_code == 200

    # Get the container ID using subprocess and docker ps command
    container_id = subprocess.check_output(['docker', 'ps', '-q'], text=True).strip()

    # Stop the Docker container using the obtained container ID
    subprocess.Popen(['docker', 'stop', container_id])

if __name__ == "__main__":
    test_docker()
