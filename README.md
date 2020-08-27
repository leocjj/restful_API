# Restful API
Restful API using our Core Technologies

![](hbnb-logo.png)

## Problem Statement: 

We have a variety of services & need to understand how they function, having the basics down for creating and communicating about how to create API’s using the tech stack below.

If there's any portion of this that isn’t familiar to you, don’t spend too much time on it as we can cover it in our working session. The goal of this activity is to quickly gauge your ability on how to function in a real work environment

(in which we would definitely expect a learning curve to get used to how we do things). Your ability to ask good questions about the things you don’t understand is a key part of this!

GitHub repository: https://github.com/leocjj/restful_API.git

Docker respository: https://hub.docker.com/r/leocjj/restful_api


## Acceptance:

1. Create a restful API using our Core Technologies

    a. Core Technologies

	    i.   Docker
	    ii.  Flask
    	iii. Python >=3.7
	    iv.  SqlAlchemy + Alembic
	    v.   Marshmallow
	    vi.  Pipenv
	    vii. PyTest

    b. Acceptance Criteria

	    i.   CRUD endpoint for a “Budget Item” using SQLAlchemy (improvise on the fields, but want to see some critical thinking)
	    ii.  example leveraging marshmallow schema for validation & serialization
	    iii. example query / migration using SQLAlchemy
	    iv.  Testing


2. Create a docker-compose to orchestrate the following https://docs.docker.com/compose/

    Flask API from Step 1

    https://github.com/localstack/localstack - Connect to preview

    MySql >= 5.7 (Docker) https://hub.docker.com/_/mysql
3. Sample Postman collection to your API (you can include the collection.json in Github)
https://www.postman.com/
4. Demonstrate connectivity between your docker network and localstack using Kinesis
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html



# First time installations
Install Docker Desktop
	https://www.docker.com/products/docker-desktop

Install git for windows
	https://git-scm.com/downloads

Vefication of Docker installation
	
	docker version
	docker run hello-world

# Instalation of restful API in a Docker container
	git clone "https://github.com/leocjj/restful_API"`
	cd restful_API
	docker build -t restfulapi .
	docker run -dp 5000:5000 --name restfulapi restfulapi



# Examples of use
To call API

	http://localhost:5000/

# Reinstallation
In case of a new code version, the old container must be stopped and deleted before a new installation.

1. Stop actual container

		docker stop restfulapi

2. Delete actual container
		
		docker rm restfulapi

3. Follow installation instructions

# Additional notes on Docker
To see Docker images available

	docker image ls

To see Docker containers

	docker ps [-a]

To publish in Docker

	docker tag restfulapi leocjj/restful_api
	docker push leocjj/restful_api

Docker Pull Command

	docker pull leocjj/restful_api


# Bugs
No known bugs at this time. 


# Authors
Leonardo Calderon - [email](mailto://leonardo.calderon@endava.com) / [Github](https://github.com/leocjj) / [Twitter](https://twitter.com/leocj)  

# Collaborators
* luisa.sepulveda
* edgar.forero
