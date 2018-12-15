CWD=/home/vagrant/nginx
cd $CWD
sudo docker build -t nginx1.7:latest .
sudo docker run -it -d -p 80:80 nginx1.7:latest