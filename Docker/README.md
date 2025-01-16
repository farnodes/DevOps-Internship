### How To Install and Use Docker on Ubuntu 22.04

Step 1 - Installing Docker 

1. First, update your existing list of packages:

```bash
sudo apt update
```

2. Next, install a few prerequisite packages which let apt use packages over HTTPS:

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

3. Then add the GPG key for the official Docker repository to your system:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

4. Add the Docker repository to APT sources:

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

5. Update your existing list of packages again for the addition to be recognized:

```bash
sudo apt update
```

6. Make sure you are about to install from the Docker repo instead of the default Ubuntu repo:

```bash
apt-cache policy docker-ce
```

7. Finally, install Docker:

```bash
sudo apt install docker-ce
```

8. Docker should now be installed, the daemon started, and the process enabled to start on boot. Check that it’s running:

```bash
sudo systemctl status docker
```

9. Check the Docker version to confirm installation:

```bash
docker --version
```


Step 2 - Verify the Installation

1. Check the Docker version to confirm installation:

```bash
docker --version
```

2 . Test Docker with a sample container:

```bash
sudo docker run hello-world
```


Step 3 - Optional - Manage Docker as a Non-Root User

1. Add your user to the docker group:

```bash
sudo usermod -aG docker $USER
```

2. Apply the changes:

```bash
newgrp docker
```

3. Test running Docker without sudo:

```bash
docker run hello-world
```


