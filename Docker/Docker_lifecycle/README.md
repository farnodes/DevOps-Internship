### Pulling a Specific Version:

```bash
docker pull ubuntu:22.04
docker pull httpd:alpine
docker pull nginx
```
### Verify Downloaded Images:

```bash
docker images
```
### List all Docker containers on your system, including 
Running containers
Stopped containers
Exited containers

```bash
docker ps -a
```


###  create and start a container from a specified Docker image. It runs the container based on the image and executes the default command

```bash
docker run [options] <image_name> [command]
```
-d: Run the container in detached mode (background).
-it: Run the container interactively with a terminal.
--name <name>: Assign a custom name to the container.
-p <host_port>:<container_port>: Map ports between the host and the container.
-v <host_dir>:<container_dir>: Mount a directory from the host into the container.


```bash
docker run -d -p 80:80 --name swetank httpd
docker run -d -p 80:80 --name anuj ngix
```

### The curl localhost command is used to send an HTTP request to your local machine

```bash
curl localhost
```

### The docker exec -it <container_name_or_id> bash command is used to start an interactive 

```bash
docker exec -it <container_name_or_id> bash
```

### Nginx & Httpd Default File Location

```bash
/usr/share/nginx/html/index.html  # nginx default config file path
/usr/local/apache2/htdocs         # httpd default congig file path
```
### default path copy 

wget free css template
unzip foldername 
cd foldername



```bash
cp . swetank:/usr/share/nginx/html/index.html # . current locatin , swetank container name 
cp . anuj:/usr/local/apache2/htdocs # . current location , anuj container name
curl localhost
```


### Continer to images create 

```bash
docker commit -a "farnodes" shi devops  # farnodes - commit kuch bhi, shi- container name, devops - images name
docker run -d -p 80:80 --name mohit devops # --name mohit container , devops - images, 
``` 

### imges Backup 

```bash
rahul@docker1:~$ docker save -o app.tar devops # imges save  and tar file
rahul@docker1:~$ docker load -i app.tar  # load imges to zip file to tar
```


