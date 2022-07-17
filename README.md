
# Getting Started

1. Clone the repository

2. Create your Heroku app: `heroku create your-app-name`

3. Push your code to Heroku with Git: `git push heroku master`


# Using Docker


Run it locally using docker


**1. Create Docker image**

```sh
docker build . -t local-shorten-python:latest
```
**2. Run the docker container**

```sh
docker run -p 8888:8000 local-shorten-python
```

**3. Verification**

Go to your browser and open http://localhost:8888
