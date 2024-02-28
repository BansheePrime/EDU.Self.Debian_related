# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "dev-debian"
  config.vm.box = "debian12"
  config.vm.hostname = "dev-debian"
  config.vm.network "private_network", ip: "192.168.56.8"
  config.vm.network "forwarded_port", guest: 22, host: 2108, id: "ssh"

  config.vm.provider "virtualbox" do |vb|
    vb.name = "dev-debian"
    vb.customize ["modifyvm", :id, "--memory", 4096]
    vb.customize ["modifyvm", :id, "--cpus", 2]
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yaml"
  end
end
