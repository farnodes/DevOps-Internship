### Docker Volume: Overview
Docker Volume is a way to persist data generated and used by Docker containers. Since containers are ephemeral (i.e., their data is lost when they are stopped or deleted), volumes provide a solution to store and manage data independently of the container lifecycle.

1. Create a Volume

```bash
docker volume create my_volume
```

2. List Volumes

```bash
docker volume ls
```

3. Inspect a Volume The docker volume inspect command provides detailed information about a specific Docker volume, such as its name, driver, mount point, and other metadata.

```bash
docker volume inspect my_volume
```

4. If you want to check where the volume's data is stored on the host system or verify its creation details, you can use docker volume inspect. For example:

```bash
docker volume inspect my_volume | grep Mountpoint
```

5. Remove a Volume

```bash
docker volume rm my_volume
```

6. The docker volume prune command is used to remove all unused volumes from your Docker system. This is particularly helpful for cleaning up volumes that are no longer being used by any containers, thus freeing up disk space.

```bash
docker volume prune
```

7. Docker, volumes are used to persist data generated or used by containers. They provide a way to store data outside the container's filesystem, ensuring that the data is not lost when a container is removed or recreated. Volumes are managed by Docker, making it easier to back up, share, and migrate data.

```bash
docker run -d -v /host/path:/container/path image_name
```
### EXAMPLE

```bash
 docker run -d  -v /home/rahul/mysql-volume:/var/lib/mysql  --name mysql -e MYSQL_ROOT_PASSWORD=root mysql:latest
```




