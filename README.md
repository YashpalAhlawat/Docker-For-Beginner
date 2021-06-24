# Docker-For-Beginner
It is a repository for simple commands to start with Docker.


###Install docker on linux, mac or windows.

Docker image--> is instruction template for any Container and is not an active entity.
Container -->is an active entity.
Deamon --> long running program




###Creating first docker container:
>docker run 'hello-world'
//It will run image hello-world if present locally. If not it will download/pull the image from dockerhub and run it locally.

>docker ps
>docker container ls
Both above command return all the container

>docker images
//it will return all the images present on the system


###RUN Ubuntu image on Docker
>docker run -it ubuntu
//-i for interactive and -t for psuedo tty (
it does is send the output to the 'virtual' tty (Bash command prompt/terminal) within this docker container. )

Kill ubuntu running docker ctrl+d,ctrl+z,exit but it will kill the running containter too.
If we want to exit from interactive shell and we want keep ubuntu docker running in background we have to run CTRL+P+Q.

But Now question is how to access the same container again. There are multiple ways to use container again 

Copy <container id> using docker ps or docker container ls and use 
>Docker attach <container id> 

	
###Container Management

Using earlier exited containers use docker ps -a copy< container id>
>docker start  < container id>

Stop a running container
>docker stop  < container id>

Forcefully stopping container
>docker kill <container id>

Removing docker from docker ps -a list
>docker rm <container id>

Printing only conatiner id 
>docker ps -aq

For removing all containers 
>docker rm $(docker ps -aq)

We cannot remove running container. It must to stopped before removing. Otherwise error will come


###Image Management

To check all images present
>docker images

To remove docker images
>docker rmi <Image id>

If we want to remove all the images
>docker rmi $(docker images -q)


To access docker private registry instead of public docker hub use 
>docker login
We can now pull from our account using
>docker pull
And also we can update any image on our account using
>docker push


###Running NGINX (Web Server) on docker
Directly pulling from reposity and running in iteractive mode
>docker run -it nginx

Running nginx container in background without goint into interactive mode and ctl+p+q to keep it alive in background
>docker run -d nginx

Running nginx image or specific port externalport:internalport
>docker run -d -p 8080:80 nginx
//we can now access nginx from local browser at 8080

Customization of Nginx home page 
>mkdir nginx
>cd nginx
>touch index.html
>vim index.html
//Write some html
Now we have to attach this volume to the 

First stop/kill nginx container
>docker kill <container id>

Default nginx page is present at /user/share/nginx/html so map it with new html page location using command as below
-v is for volume
>docker run -d -p 8080:80 -v $(PWD)/nginx:/user/share/nginx/html nginx



###DOCKERFILE

Must create a file with same name Dockerfile.

Write Dockerfile content as below to create custom image
FROM  <Iamge Name>:<version>
RUN <command>
CMD
ENTRYPOINT
ADD <src> <dest> 
WORKDIR <PATH WILL BE PWD>
ENV <define environment variables >

After saving run
>docker build .
// . If directory is same where Dockerfile present else use docker build -f <Path of Dockerfile>

For building Dockerfile with image name and tag
>docker build -t <imageName>:<tag> .




ENTRYPOINT-->it will be appended to every command we provide from running terminal for docker build
CMD-->Run command, if not provided any command it will not executed(default command ) if no argument provided while docker build command
RUN-->Run Command
ADD --> copy file build directories
WORKDIR-->value work as current directory (combination of mkdir+CD)
ENV-->define environment Variable 
COPY ->copy external host to internal host



###Docker Compose

Used to define multi container application

YAML stands for (Yet Another Markup Language)

Example syntax for YAML is given below :

---
#comment list of fruits
	- Apple
	- Banana
	- Strawberry
	- Pear
	- Mango


#another example Employee record
Martin:
  name:Martin
  job:Manager
  skills:python



Two spaces between the main group and subgroups



Compose Dockerfile for flask app(use requirements.txt which contains flask and redis)
Create Dockerfile in same directory
Write in Dockerfile as below
FROM python:3.7-alpine
WORKDIR  /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST = 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 500
CMD ["flask","run"]

Create docker compose file
>touch docker-compose.yml
>vim docker-compose.yml
Version:"3.8"
Services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      -  .:/code
  redis:
    image:"redis:alpine"


>docker-compose up
>docker-compose up -d
>docker-compose down



![image](https://user-images.githubusercontent.com/18135348/123264718-ee113000-d517-11eb-9ea3-bb9b1f814002.png)
