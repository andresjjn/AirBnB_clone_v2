#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get install -y nginx
sudo ufw allow 'Nginx HTTP'
if [ ! -d "data" ]; then
    mkdir -p data;
fi
if [ ! -d "/data/web_static" ]; then
    mkdir -p /data/web_static;
fi
if [ ! -d "/data/web_static/releases" ]; then
    mkdir -p /data/web_static/releases;
fi
if [ ! -d "/data/web_static/shared" ]; then
    mkdir -p /data/web_static/shared;
fi
if [ ! -d "/data/web_static/releases/test" ]; then
    mkdir -p perro/data;
fi
{
    echo "<!DOCTYPE html>"
    echo "<html lang=\"en\">"
    echo "<head>"
	echo "    <meta charset=\"UTF-8\">"
	echo "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"
	echo "    <title>Test</title>"
    echo "</head>"
    echo "<body>"
	echo "    <h1>DocApp</h1>"
    echo "</body>"
    echo "</html>"
} > /data/web_static/releases/test/index.html
if [ -d "/data/web_static/releases/test" ]; then
    sudo rm -r /data/web_static/releases/test
    sudo ln -s /data/web_static/current /data/web_static/releases/test/
else
    sudo ln -s /data/web_static/current /data/web_static/releases/test/
fi
sudo chmod -R ubuntu:ubuntu data
sudo sed -i '33i \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart