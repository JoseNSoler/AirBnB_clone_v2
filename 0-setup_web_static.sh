#!/usr/bin/env bash
# Install and update nginx to deploy web_static

sudo apt-get update
sudo apt-get install -y nginx


sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo touch /data/web_static/releases/test/index.html

printf %s "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html

sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

printf %s "server {
    listen      80 default_server;
    listen      [::]:80 default_server;
    root        /etc/nginx/html;
    index       index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current/;
    }
}
" > /etc/nginx/sites-available/default

sudo service nginx restart