# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/xenial64"

  
  # Vagrant Network Provisions and Ubuntu apt configuration
  # config.vm.provision "file", source: "./ansible", destination: "$HOME/workdir"
  # config.vm.synced_folder ".", "/vagrant", type: "nfs"
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update -y
    sudo apt-get -y upgrade
    sudo apt-get install -y software-properties-common python-software-properties
    sudo add-apt-repository ppa:jonathonf/python-3.6
    sudo apt-get update -y
    sudo apt-get install -y python3.6
    sudo apt-get install -y python3-pip
  SHELL
  # config.vm.provision :shell, path: "scripts/bootstrap.sh"

  config.vm.network "private_network", type: "dhcp"
  config.vm.network "forwarded_port", guest: 8080, host: 8080, host_ip: "127.0.0.1"
  # config.vm.network "forwarded_port", guest: 8081, host: 8081, host_ip: "127.0.0.1"
  # config.vm.network "forwarded_port", guest: 8082, host: 8082, host_ip: "127.0.0.1"
  
  # Ansible and Docker installation
  config.ssh.insert_key = false
  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "scripts/docker_install.yml"
  end
  
  # Nginx installation 
  config.vm.provision "file", source: "./nginx", destination: "/home/vagrant/nginx"
  # config.vm.provision :shell, path: "scripts/build_nginx.sh"

  # Microservice-1 dockers
  config.vm.provision "file", source: "./app", destination: "/home/vagrant/app"
  config.vm.provision "shell", inline: <<-SHELL
    CWD=/home/vagrant/app
    cd $CWD
    sudo docker-compose build
    sudo docker-compose up -d
  SHELL
end
