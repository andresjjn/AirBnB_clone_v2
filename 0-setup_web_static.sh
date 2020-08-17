#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get install -y nginx
sudo ufw allow 'Nginx HTTP'
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
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
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '33i \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart
