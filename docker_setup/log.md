## start container from node latest image, set name and open shell inside container

docker run --name gidra-nodejs -it node /usr/bin/bash

docker run --name gidra-python -it python /usr/bin/bash

### run as root

apt update
apt install sudo
useradd -m admin
echo -e "123\n123" | passwd admin
usermod -aG sudo admin
su admin

### run as admin

sudo apt install -y git vim
sudo vim /etc/passwd

#### change root shell to nologin option

/bin/bash --> /usr/sbin/nologin

#### change admin shell to bash

/bin/sh --> /bin/bash

### download vimrc file by method of your choice

wget --no-check-certificate --content-disposition {INSER file location here} ~/
``or``
curl -LJO {INSER file location here}

### connect to container
docker exec -it {container name} bash

#### node.js case
docker exec -it --user admin gidra-nodejs bash
#### python case
docker exec -it --user admin gidra-python bash
#### textual case
docker exec -it --user dev developer bash