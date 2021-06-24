# Docker-For-Beginner

It is a repository for simple commands to start with Docker.

### Install docker on linux, mac or windows

Docker image--> is instruction template for any Container and is not an active entity.
Container -->is an active entity.
Deamon --> long running program.

### Creating first docker container

```console
>docker run 'hello-world'
```

It will run image hello-world if present locally. If not it will download/pull the image from dockerhub and run it locally.

```console
>docker ps
>docker container ls
```
Both above command return all the container present

```console
>docker images
```
//it will return all the images present on the system


### RUN Ubuntu image on Docker
```console
>docker run -it ubuntu
```
//-i for interactive and -t for psuedo tty (
it does is send the output to the 'virtual' tty (Bash command prompt/terminal) within this docker container. )

Kill ubuntu running docker ctrl+d,ctrl+z,exit but it will kill the running containter too.
If we want to exit from interactive shell and we want keep ubuntu docker running in background we have to run <kbd>CTRL</kbd>+<kbd>P</kbd>+<kbd>Q</kbd>.

But Now question is how to access the same container again. There are multiple ways to use container again 

Copy <container id> using docker ps or docker container ls and use 
```console
>Docker attach <container id> 
```
 
### Container Management

Using earlier exited containers use docker ps -a copy< container id>
```console
>docker start  < container id>
```
Stop a running container
```console
>docker stop  < container id>
```

Forcefully stopping container
```console
>docker kill <container id>
```

Removing docker from docker ps -a list
```console
>docker rm <container id>
```

Printing only conatiner id 
```console
>docker ps -aq
```

For removing all containers 
```console
>docker rm $(docker ps -aq)
```
We cannot remove running container. It must to stopped before removing. Otherwise error will come


### Image Management

To check all images present
```console
>docker images
```
To remove docker images
```console
>docker rmi <Image id>
```
If we want to remove all the images
```console
>docker rmi $(docker images -q)
```

To access docker private registry instead of public docker hub use 
```console
>docker login
```
We can now pull from our account using
```console
>docker pull
```
And also we can update any image on our account using
```console
>docker push
```

### Running NGINX (Web Server) on docker
Directly pulling from reposity and running in iteractive mode
```console
>docker run -it nginx
```
Running nginx container in background without goint into interactive mode and ctl+p+q to keep it alive in background
```console
>docker run -d nginx
```
Running nginx image or specific port externalport:internalport
```console
>docker run -d -p 8080:80 nginx
```
we can now access nginx from local browser at 8080

### Customization of Nginx home page 
```console
>mkdir nginx
>cd nginx
>touch index.html
>vim index.html
```
//Write some html
Now we have to attach this volume to the 

First stop/kill nginx container
```console
>docker kill <container id>
```
Default nginx page is present at /user/share/nginx/html so map it with new html page location using command as below
-v is for volume
```console
>docker run -d -p 8080:80 -v $(PWD)/nginx:/user/share/nginx/html nginx
```

### DOCKERFILE

Must create a file with same name Dockerfile.
```docker
Write Dockerfile content as below to create custom image
FROM  <Iamge Name>:<version>
RUN <command>
CMD
ENTRYPOINT
ADD <src> <dest> 
WORKDIR <PATH WILL BE PWD>
ENV <define environment variables >
```
After saving run
```console
>docker build .
```
// . If directory is same where Dockerfile present else use 
```console
docker build -f <Path of Dockerfile>
```

For building Dockerfile with image name and tag
```console
>docker build -t <imageName>:<tag> .
```



**ENTRYPOINT**-->it will be appended to every command we provide from running terminal for docker build
**CMD**-->Run command, if not provided any command it will not executed(default command ) if no argument provided while docker build command
**RUN**-->Run Command
**ADD** --> copy file build directories
**WORKDIR**-->value work as current directory (combination of mkdir+CD)
**ENV**-->define environment Variable 
**COPY** ->copy external host to internal host


### Docker Compose

Used to define multi container application

YAML stands for (Yet Another Markup Language)

Example syntax for YAML is given below :
```YAML
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

```

**Two spaces between the main group and subgroups**

### Compose Dockerfile for flask app(use requirements.txt which contains flask and redis)  
- Create Dockerfile in same directory
- Write in Dockerfile as below
```YAML
FROM python:3.7-alpine
WORKDIR  /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST = 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 500
CMD ["flask","run"]
```

- Create docker compose file
```bash
>touch docker-compose.yml
>vim docker-compose.yml
```
```YAML
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
```
```console
>docker-compose up
>docker-compose up -d
>docker-compose down
```
 Feel free to contribute to it. To know more about me <a  href='https://yashpalahlawat.github.io/vitae/'>Click Here</a>.
