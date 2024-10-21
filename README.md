**System Monitoring**<br/>
The end goal of this project is develop a REST API which monitors and tracks system resources including CPU, Memeory, disk spce and bandwidth usage.
The API is containerized and with Docker and deployed on EC2 for better scalability. A systemd service is used to ensure the API runs as a daemon for continuous monitoring.</br>
<br/>

**Features**
* Installation
* API Endpoints
* Technologies Used

**Installation**<br/>
The API will require to install few softwares. This will be done automatically when the the docker image is pulled from the docker hub and ran.
But for better understanding of the requirements, below are steps to install the softwares.<br/>
* sudo apt-get install -y python3 python3-pip
* sudo pip3 install django
* pip install django

**Steps to use the API**
* Create a EC2 instance
* Install docker to pull and run the docker image --> sudo yum install docker
* sudo systemctl start docker
* Pull the docker image from the dockerhub --> sudo docker pull m4h1m4/rest_api:latest
* Run the docker image with the command --> sudo docker run -d -p 8000:8000 m4h1m4/rest_api
* Access the API with the required end point with curl command --> curl -L -H "Authorization:CS218" http://localhost:8000/api/cpu
* Replace "cpu" with "disk", "memory", "bandwidth" as per necissity.

**API Endpoints**
The API provides the following endpoints for system metrics:
* GET /api/cpu: Get real-time CPU usage
* GET /api/memory: Get real-time memory usage
* GET /api/disk: Get real-time disk usage
* GET /api/bandwidth: Get real-time bandwidth usage 

**Technologies Used**
* Django: Web Framework for building the REST API
* Docker: Containerization for consistent deployments
* AWS EC2: Cloud Infrastructure for hosting the API
* systemd: To run the API as a daemon
* Python: Backend logic and API deployment
  







