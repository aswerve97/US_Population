# US Population ReadMe

This projection is the deployment side of predicting US population. If you would
like to see the developement and some of the Exploratory Data Analysis 

## Instructions on how to deploy to Docker

### These configuartions are confirmed to work 
docker run -d -p 8080:5000 DOCKER_IMAGE_NAME_GOES_HERE

Dockerfile
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]