# US Population ReadMe

This projection is the deployment side of predicting US population. If you would
like to see the developement and some of the Exploratory Data Analysis 

## Instructions on how to deploy to Docker

### These configuartions are confirmed to work 
docker run -d -p 8080:5000 DOCKER_IMAGE_NAME_GOES_HERE

Dockerfile
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]

Upon further investigation, you do not have to give your flask app 
a default port to get docker to work. Instead so far you can just tell docker to use host=0.0.0.0 and then docker will run the flask app, flask app will set up the defailt port of 5000 and then you are able to access it locally that port that is exposed via docker so local:docker so 8080:5000 is valid