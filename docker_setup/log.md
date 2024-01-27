## start container from node latest image, set name and open shell inside container
docker run --name gidra-nodejs -it node /usr/bin/bash

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
wget --no-check-certificate --content-disposition https://github.com/BansheePrime/EDU.Self.Debian_related/blob/b0381752b41bc59fc86712a83642f5f943d30949/vim_setup/.vimrc ~/
``or``
curl -LJO https://github.com/BansheePrime/EDU.Self.Debian_related/blob/b0381752b41bc59fc86712a83642f5f943d30949/vim_setup/.vimrc

### connect to container
docker exec -it {container name} bash
docker exec -it --user admin gidra-nodejs bash